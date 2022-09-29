import pdb
import numpy as np

class TDPlotter:
  marker1 = np.array([[0, 0, 1, 1, 1, 0, 0],
                      [0, 1, 1, 0, 1, 1, 0],
                      [1, 1, 0, 0, 0, 1, 1],
                      [1, 1, 0, 1, 0, 1, 1],
                      [1, 1, 0, 0, 0, 1, 1],
                      [0, 1, 1, 0, 1, 1, 0],
                      [0, 0, 1, 1, 1, 0, 0]], dtype=float)
  marker1_xoff = 4
  marker1_yoff = 4

  def __init__(self, w, h):
    self.plot_bitmap = np.zeros((h,w,3), dtype=np.uint8)
    self.w = w
    self.h = h

  def resize(self, w, h):
    self.plot_bitmap = np.zeros((h,w,3), dtype=np.uint8)
    self.w = w
    self.h = h

  def plot_XY(self, x, y, m=None, ylim=None, xlim=None):
    """
    for each coordinate, plot pixel 
    """
    if ylim is None:
      range_y = max(y) - min(y)
      min_y   = min(y)
      max_y   = max(y)
    else:
      range_y = ylim[1] - ylim[0]
      min_y   = ylim[0]
      max_y   = ylim[1]

    if xlim is None:
      range_x = max(x) - min(x)
      min_x   = min(x)
      max_x   = max(x)
    else:
      range_x = xlim[1] - xlim[0]
      min_x   = xlim[0]
      max_x   = xlim[1]

    #x_crop = [x_val for x_val in x if x_val >= min_x and x_val <= max_x]
    #y_crop = [y_val for y_val in x if y_val >= min_y and y_val <= max_y]

    x_plot = [int((x_val - min_x) * self.w / range_x) for x_val in x]
    y_plot = [int(self.h - (y_val - min_y) * self.h / range_y) for y_val in y]
    x_plot_cropper = [x_val >= 0 and x_val < self.w for x_val in x_plot]
    y_plot_cropper = [y_val >= 0 and y_val < self.h for y_val in y_plot]
    combo_cropper = list(np.where(np.logical_and(x_plot_cropper, y_plot_cropper))[0])
    #pdb.set_trace()
    y_plot = [y_plot[idx] for idx in combo_cropper]
    x_plot = [x_plot[idx] for idx in combo_cropper]
    #x_plot = [x_val for x_val in x_plot if x_val >= 0 and x_val < self.w]
    #y_plot = [y_val for y_val in y_plot if y_val >= 0 and y_val < self.h]
    self.plot_bitmap[:] = 0
    self.plot_bitmap[y_plot, x_plot, :] = np.array([200, 200, 150], dtype=np.uint8)
      
  
