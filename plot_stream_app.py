import wx
from wx import MessageDialog
from threading import Thread
from time import sleep

#from streamplotterapp import record_app_functionality
from streamplotterapp.forms import record_app_forms
from packetprocessor import serial_recorder, packet_processor, file_streamer
from td_plot.plotter import TDPlotter


#serial_rec = serial_recorder.SerialRecorder("/dev/ttyUSB0")
#packer = packet_processor.PacketProcessorManager()
#myplt = TDPlotter(300, 200)
#myplt.plot_XY([-100, 0, 10, 4, -4], [-10, 10, -10, 4, 4], ylim=[-40, 40], xlim = [-80, 80])

xcoords = [-40]
ycoords = [-40]

class MainWindowFunctional (record_app_forms.MainWindow):
  def __init__(self, parent):
    super().__init__(parent)
    self.plot_update_thread = None
    self.plot_update_stop_req = False
    self.serial_rec = None
    self.serial_dev = None

    self.packer = packet_processor.PacketProcessorManager()
    self.file_streamer = None

    self.plot1_update(None)
    #self.main_frame_resize_clbk(None)
    self.plot_w = 100
    self.plot_h = 100
    self.tdp = TDPlotter(self.plot_w, self.plot_h)
    self.tdp.plot_XY([-100, 0, 10, 4, -4], [-10, 10, -10, 4, 4], ylim=[-40, 40], xlim = [-80, 80])
    self.plot_image = wx.Bitmap.FromBuffer(self.tdp.w, self.tdp.h, self.tdp.plot_bitmap)

  def open_pressed_clbk(self, event):
    self.serial_dev = self.m_textCtrlInputDevice.GetValue()
    try:
      self.serial_rec = serial_recorder.SerialRecorder(self.serial_dev)
      with MessageDialog(self, "Success!") as md:
        md.ShowModal()
    except Exception as e:
      # Raise dialog
      with MessageDialog(self, "Unable to open {0} because: \n{1}".format(
                  self.serial_dev, str(e))) as md:
        md.ShowModal()
      self.serial_rec = None

  def record_pressed_clbk(self, event):
    print("Record Pressed!")
    self.serial_rec.start_recording_session()
    self.packer.start_watch_list(self.serial_rec.bytelist)
  
  def stop_pressed_clbk(self, event):
    print("Stop Pressed!")
    self.serial_rec.stop()
    self.packer.stop_when_done()
    print("All packets processed.")
    expected_packet_no =  len(self.serial_rec.bytelist) / 14.0
    print("Got {0} packets from {1} bytes: {2:.4%} received of total expected".format(
          len(self.packer.packet_list), len(self.serial_rec.bytelist), 
          len(self.packer.packet_list) / expected_packet_no))
    valid_packets = [packet for packet in self.packer.packet_list if packet["crc_valid"]]
    print("{0} packets had valid CRC: {1:.4%} valid of total expected".format(
          len(valid_packets), len(valid_packets) / expected_packet_no))

  def show_hide_pressed_clbk(self, event):
    print("Show Hide Pressed!")
    if self.plot_update_thread is None:
      print("Show!")
      self.plot_panel.Show()
      self.m_bitmap2.SetBitmap(wx.Bitmap.FromBuffer(self.tdp.w, self.tdp.h, self.tdp.plot_bitmap))
      self.m_bitmap2.Update()
      self.m_bitmap2.Refresh()
      self.plot_panel.Update()
      self.plot_panel.Layout()
      self.Update()
      self.Layout()
      self.Update()
      self.start_plot()
    else:
      print("Hide!")
      self.stop_plot()
      self.plot_panel.Hide()
      self.Layout()
    # if thread not started, Start thread to:
    #  1. update displayed bitmap contents 
    #  2. trigger write to screen frequently
    #  3. check if it should stop
    # else stop thread

  def plot_file_clbk(self, event, repeat=False):
    # Open file picker
    with wx.FileDialog(self, "Open recorded file", 
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
      if fileDialog.ShowModal() == wx.ID_CANCEL:
        return
      pathname = fileDialog.GetPath()
    # Open chosen file with file streamer
    # Set watchlist for packer to file stream
      try:
        self.file_streamer = file_streamer.FileStreamer(pathname, repeat=repeat)
        self.packer.start_watch_list(self.file_streamer.byte_list)
      except Exception as e:
        with MessageDialog(self, "Unable to open {0} because: \n{1}".format(
                           pathname, str(e))) as md:
          md.ShowModal()
        self.file_streamer = None
    

  def plot_file_loop_clbk(self, event):
    self.plot_file_clbk(event, repeat=True)

  def update_and_draw(self):
    ycoords = []
    xcoords = []
    while not self.plot_update_stop_req:
      if len(xcoords) < len(self.packer.valid_packet_list): # track packets
        ycoords.extend([packet["chan_a"] for packet in self.packer.valid_packet_list[len(ycoords):-1]])
        xcoords.extend([packet["seq"] for packet in self.packer.valid_packet_list[len(xcoords):-1]])
      if self.tdp.w != self.plot_w or self.tdp.h != self.plot_h: # if resize needed
        print("resize_atmp", end='', flush=True)
        self.tdp.resize(self.plot_w, self.plot_h)
        print(self.tdp.w, self.tdp.h)
      if len(xcoords) > 0: 
        x_high = max(self.min_window_len, max(xcoords))
        x_low = max(0, x_high - self.max_window_len)
      else:
        x_high = self.min_window_len
        x_low = 0
      self.tdp.plot_XY(xcoords,ycoords, ylim=[self.P1YMin, self.P1YMax], xlim = [x_low, x_high])
      self.plot_image = wx.Bitmap.FromBuffer(self.tdp.w, self.tdp.h, self.tdp.plot_bitmap)
      self.m_bitmap2.SetBitmap(self.plot_image)
      print("plotted", end='', flush=True)
      sleep(0.2)
      #self.m_bitmap2.Update()
      #self.m_bitmap2.Refresh()

  def main_frame_resize_clbk(self, event):
    #import pdb; pdb.set_trace()
    # get size of base window, get size of child windows
    # any sizer with the same x should have the height subtracted from the plot area
    # all other sizers are assumed to be on the right side and have their width subtracted
    # the remaining area is the plot area
    self.Update()
    base_size = self.GetSizer().GetSize()
    plot_w = base_size.x
    plot_h = base_size.y
    rec_cont_size = self.GetSizer().GetChildren()[0].GetSize()
    input_size    = self.GetSizer().GetChildren()[1].GetSize()
    plt_cont_size = self.plot_panel.GetSizer().GetChildren()[1].GetSize()
    self.plot_w = max(10,plot_w - plt_cont_size.x)
    self.plot_h = max(10,plot_h - input_size.y - rec_cont_size.y)
    self.m_bitmap2.SetBitmap(wx.Bitmap(self.plot_w, self.plot_h))
    print(base_size, rec_cont_size, input_size, plt_cont_size, self.plot_w, self.plot_h)
    self.Layout()
    self.Update()
    # set plot window sizes to space left over from 
    # controls, input pickers and plot controls

  def plot1_update(self, event):
    # Update plot 1 size from text boxes
    self.min_window_len = int(self.m_textCtrlP1WinMin.GetValue())
    self.max_window_len = int(self.m_textCtrlP1WinMax.GetValue())
    self.P1YMin = int(self.m_textCtrlP1YMin.GetValue())
    self.P1YMax = int(self.m_textCtrlP1YMax.GetValue())

  def stop_plot(self):
    print("stop called", end='', flush=True)
    if self.plot_update_thread is not None:
      print("stopping plot")
      self.plot_update_stop_req = True
      self.plot_update_thread.join()
      self.plot_update_thread = None

  def start_plot(self):
    if self.plot_update_thread is None:
      self.plot_update_stop_req = False
      self.plot_update_thread = Thread(target = self.update_and_draw)
      self.plot_update_thread.start()

  def close_app_clbk(self, event):
    self.stop_plot()    
    # also stop other running threads
    event.Skip() # let nature run its course

if __name__ == '__main__':
  app = wx.App()

  mainframe = MainWindowFunctional(None)
  mainframe.Show()
  app.MainLoop()
