from .forms import record_app_forms

class MainWindowFunctional (record_app_forms.MainWindow):
  def record_pressed_clbk(self, event):
    print("Record Pressed!")
  
  def stop_pressed_clbk(self, event):
    print("Stop Pressed!")