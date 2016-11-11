# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class PanelUno
###########################################################################

class PanelUno ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 720,190 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.btn_clientes = wx.Button( self, wx.ID_ANY, u"Buscar cliente", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_clientes.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_clientes, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btn_modificar = wx.Button( self, wx.ID_ANY, u"Modificar", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.btn_modificar.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.btn_modificar.Enable( False )
		
		gbSizer1.Add( self.btn_modificar, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.grilla_uno = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 670,135 ), 0 )
		
		# Grid
		self.grilla_uno.CreateGrid( 0, 6 )
		self.grilla_uno.EnableEditing( False )
		self.grilla_uno.EnableGridLines( True )
		self.grilla_uno.EnableDragGridSize( False )
		self.grilla_uno.SetMargins( 0, 0 )
		
		# Columns
		self.grilla_uno.SetColSize( 0, 80 )
		self.grilla_uno.SetColSize( 1, 200 )
		self.grilla_uno.EnableDragColMove( False )
		self.grilla_uno.EnableDragColSize( True )
		self.grilla_uno.SetColLabelSize( 30 )
		self.grilla_uno.SetColLabelValue( 0, u"Código" )
		self.grilla_uno.SetColLabelValue( 1, u"Apellido y nombre" )
		self.grilla_uno.SetColLabelValue( 2, u"Monto" )
		self.grilla_uno.SetColLabelValue( 3, u"Entregado" )
		self.grilla_uno.SetColLabelValue( 4, u"Boleta" )
		self.grilla_uno.SetColLabelValue( 5, u"Recibo" )
		self.grilla_uno.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grilla_uno.AutoSizeRows()
		self.grilla_uno.EnableDragRowSize( True )
		self.grilla_uno.SetRowLabelSize( 50 )
		self.grilla_uno.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grilla_uno.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		gbSizer1.Add( self.grilla_uno, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
	
	def __del__( self ):
		pass
	

