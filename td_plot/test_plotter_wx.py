import wx
import pdb

from plotter import TDPlotter

class Frame(wx.Frame):
  def __init__(self, bitmap_in, parent=None, id=-1,pos=wx.DefaultPosition, title='wxPython'):
    size = (myplt.w, myplt.h)
    wx.Frame.__init__(self, parent, id, title, pos, size)
    self.bmp = wx.StaticBitmap(parent=self, bitmap=bitmap_in)
    self.SetClientSize(size)

class App(wx.App):
  def OnInit(self):
    pdb.set_trace()
    image = wx.Bitmap.FromBuffer(myplt.w, myplt.h, myplt.plot_bitmap)           
    self.frame = Frame(image)
    self.frame.Show()
    self.SetTopWindow(self.frame)
    return True


print("Making plot")
myplt = TDPlotter(200, 200)
myplt.plot_XY([-10, 0, 10, 4, -4], [-10, 10, -10, 4, 4], ylim=[-40, 40], xlim = [-20, 20])
print("Plot in memory")

app = App()
app.MainLoop()
