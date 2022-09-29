# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainWindow
###########################################################################

class MainWindow ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"reDAQ - DAQ recording app", pos = wx.DefaultPosition, size = wx.Size( 497,656 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizerBase = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizerBase.AddGrowableCol( 0 )
		fgSizerBase.SetFlexibleDirection( wx.BOTH )
		fgSizerBase.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizerControls = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizerControls.AddGrowableCol( 2 )
		fgSizerControls.SetFlexibleDirection( wx.BOTH )
		fgSizerControls.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_rec_button = wx.Button( self, wx.ID_ANY, u"Record", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerControls.Add( self.m_rec_button, 0, wx.ALL, 5 )

		self.m_stop_rec_button = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerControls.Add( self.m_stop_rec_button, 0, wx.ALL, 5 )

		self.m_gauge_rec = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_rec.SetValue( 0 )
		fgSizerControls.Add( self.m_gauge_rec, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_plot_toggle_button = wx.Button( self, wx.ID_ANY, u"Show/Hide Plot", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerControls.Add( self.m_plot_toggle_button, 0, wx.ALL, 5 )


		fgSizerBase.Add( fgSizerControls, 1, wx.EXPAND, 5 )

		fgSizerInputFile = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizerInputFile.AddGrowableCol( 1 )
		fgSizerInputFile.SetFlexibleDirection( wx.BOTH )
		fgSizerInputFile.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticTextInputDevice = wx.StaticText( self, wx.ID_ANY, u"Input Device: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextInputDevice.Wrap( -1 )

		self.m_staticTextInputDevice.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizerInputFile.Add( self.m_staticTextInputDevice, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.AddGrowableCol( 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_textCtrlInputDevice = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		fgSizer6.Add( self.m_textCtrlInputDevice, 1, wx.ALL|wx.EXPAND, 5 )

		self.open_dev_button = wx.Button( self, wx.ID_ANY, u"Open!", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.open_dev_button, 0, wx.ALL, 5 )


		fgSizerInputFile.Add( fgSizer6, 1, wx.EXPAND, 5 )

		self.m_staticTextOutputDir = wx.StaticText( self, wx.ID_ANY, u"Output Dir: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextOutputDir.Wrap( -1 )

		fgSizerInputFile.Add( self.m_staticTextOutputDir, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_USE_TEXTCTRL )
		fgSizerInputFile.Add( self.m_dirPicker1, 1, wx.ALL|wx.EXPAND, 5 )


		fgSizerBase.Add( fgSizerInputFile, 1, wx.EXPAND, 5 )

		fgSizerPlot = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizerPlot.SetFlexibleDirection( wx.BOTH )
		fgSizerPlot.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.plot_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.AddGrowableCol( 0 )
		fgSizer5.AddGrowableCol( 1 )
		fgSizer5.AddGrowableRow( 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer8 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer8.AddGrowableCol( 0 )
		fgSizer8.AddGrowableRow( 0 )
		fgSizer8.AddGrowableRow( 1 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap2 = wx.StaticBitmap( self.plot_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_bitmap2, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_bitmap3 = wx.StaticBitmap( self.plot_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer8.Add( self.m_bitmap3, 1, wx.ALL|wx.EXPAND, 5 )


		fgSizer5.Add( fgSizer8, 1, wx.EXPAND, 5 )

		fgSizerPlotControls = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizerPlotControls.SetFlexibleDirection( wx.BOTH )
		fgSizerPlotControls.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self.plot_panel, wx.ID_ANY, u"Min Width", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizerPlotControls.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_textCtrlP1WinMin = wx.TextCtrl( self.plot_panel, wx.ID_ANY, u"10000", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		fgSizerPlotControls.Add( self.m_textCtrlP1WinMin, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self.plot_panel, wx.ID_ANY, u"Max Width", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizerPlotControls.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_textCtrlP1WinMax = wx.TextCtrl( self.plot_panel, wx.ID_ANY, u"40000", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		fgSizerPlotControls.Add( self.m_textCtrlP1WinMax, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self.plot_panel, wx.ID_ANY, u"Plot1 Y Min", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizerPlotControls.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrlP1YMin = wx.TextCtrl( self.plot_panel, wx.ID_ANY, u"2500", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		fgSizerPlotControls.Add( self.m_textCtrlP1YMin, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self.plot_panel, wx.ID_ANY, u"Plot1 Y Max", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizerPlotControls.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_textCtrlP1YMax = wx.TextCtrl( self.plot_panel, wx.ID_ANY, u"2700", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		fgSizerPlotControls.Add( self.m_textCtrlP1YMax, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self.plot_panel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizerPlotControls.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self.plot_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerPlotControls.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self.plot_panel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizerPlotControls.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self.plot_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerPlotControls.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.plot_panel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizerPlotControls.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self.plot_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerPlotControls.Add( self.m_textCtrl10, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self.plot_panel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizerPlotControls.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self.plot_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerPlotControls.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self.plot_panel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizerPlotControls.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self.plot_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerPlotControls.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self.plot_panel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizerPlotControls.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self.plot_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerPlotControls.Add( self.m_textCtrl13, 0, wx.ALL, 5 )


		fgSizer5.Add( fgSizerPlotControls, 1, wx.EXPAND, 5 )


		self.plot_panel.SetSizer( fgSizer5 )
		self.plot_panel.Layout()
		fgSizer5.Fit( self.plot_panel )
		fgSizerPlot.Add( self.plot_panel, 1, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )


		fgSizerBase.Add( fgSizerPlot, 1, wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		self.SetSizer( fgSizerBase )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Plot File", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Plot File (Loop)", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.close_app_clbk )
		self.Bind( wx.EVT_SIZE, self.main_frame_resize_clbk )
		self.m_rec_button.Bind( wx.EVT_BUTTON, self.record_pressed_clbk )
		self.m_stop_rec_button.Bind( wx.EVT_BUTTON, self.stop_pressed_clbk )
		self.m_plot_toggle_button.Bind( wx.EVT_BUTTON, self.show_hide_pressed_clbk )
		self.m_textCtrlInputDevice.Bind( wx.EVT_TEXT_ENTER, self.open_pressed_clbk )
		self.open_dev_button.Bind( wx.EVT_BUTTON, self.open_pressed_clbk )
		self.m_textCtrlP1WinMin.Bind( wx.EVT_TEXT_ENTER, self.plot1_update )
		self.m_textCtrlP1WinMax.Bind( wx.EVT_TEXT_ENTER, self.plot1_update )
		self.m_textCtrlP1YMin.Bind( wx.EVT_TEXT_ENTER, self.plot1_update )
		self.m_textCtrlP1YMax.Bind( wx.EVT_TEXT_ENTER, self.plot1_update )
		self.Bind( wx.EVT_MENU, self.plot_file_clbk, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.plot_file_loop_clbk, id = self.m_menuItem2.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def close_app_clbk( self, event ):
		event.Skip()

	def main_frame_resize_clbk( self, event ):
		event.Skip()

	def record_pressed_clbk( self, event ):
		event.Skip()

	def stop_pressed_clbk( self, event ):
		event.Skip()

	def show_hide_pressed_clbk( self, event ):
		event.Skip()

	def open_pressed_clbk( self, event ):
		event.Skip()


	def plot1_update( self, event ):
		event.Skip()




	def plot_file_clbk( self, event ):
		event.Skip()

	def plot_file_loop_clbk( self, event ):
		event.Skip()


