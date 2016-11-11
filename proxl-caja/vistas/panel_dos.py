# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class PanelDos
###########################################################################

class PanelDos ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 720,190 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.btn_ingresos = wx.Button( self, wx.ID_ANY, u"Ingresos varios", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_ingresos.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_ingresos, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btn_egresos = wx.Button( self, wx.ID_ANY, u"Egresos varios", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_egresos.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_egresos, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.grilla_dos = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 670,135 ), 0 )
		
		# Grid
		self.grilla_dos.CreateGrid( 0, 3 )
		self.grilla_dos.EnableEditing( True )
		self.grilla_dos.EnableGridLines( True )
		self.grilla_dos.EnableDragGridSize( False )
		self.grilla_dos.SetMargins( 0, 0 )
		
		# Columns
		self.grilla_dos.SetColSize( 0, 120 )
		self.grilla_dos.SetColSize( 1, 80 )
		self.grilla_dos.SetColSize( 2, 400 )
		self.grilla_dos.EnableDragColMove( False )
		self.grilla_dos.EnableDragColSize( True )
		self.grilla_dos.SetColLabelSize( 30 )
		self.grilla_dos.SetColLabelValue( 0, u"Tipo" )
		self.grilla_dos.SetColLabelValue( 1, u"Monto" )
		self.grilla_dos.SetColLabelValue( 2, u"Concepto" )
		self.grilla_dos.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grilla_dos.AutoSizeRows()
		self.grilla_dos.EnableDragRowSize( True )
		self.grilla_dos.SetRowLabelSize( 50 )
		self.grilla_dos.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grilla_dos.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		gbSizer1.Add( self.grilla_dos, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 6 ), wx.ALL, 5 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
	
	def __del__( self ):
		pass
	

