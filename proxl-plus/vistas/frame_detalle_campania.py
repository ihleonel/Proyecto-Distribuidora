# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class FrameDetalleCampania
###########################################################################

class FrameDetalleCampania ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Detalle de campaña", pos = wx.DefaultPosition, size = wx.Size( 945,510 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.st_titulo = wx.StaticText( self, wx.ID_ANY, u"Listado de", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_titulo.Wrap( -1 )
		self.st_titulo.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.st_titulo, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 20 )
		
		self.btn_generar = wx.Button( self, wx.ID_ANY, u"Generar reporte", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.btn_generar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_generar, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.LEFT, 20 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.grilla = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 870,300 ), 0 )
		
		# Grid
		self.grilla.CreateGrid( 0, 8 )
		self.grilla.EnableEditing( True )
		self.grilla.EnableGridLines( True )
		self.grilla.EnableDragGridSize( False )
		self.grilla.SetMargins( 0, 0 )
		
		# Columns
		self.grilla.SetColSize( 0, 80 )
		self.grilla.SetColSize( 1, 280 )
		self.grilla.SetColSize( 2, 80 )
		self.grilla.SetColSize( 3, 200 )
		self.grilla.SetColSize( 4, 80 )
		self.grilla.SetColSize( 5, 80 )
		self.grilla.SetColSize( 6, 170 )
		self.grilla.SetColSize( 7, 170 )
		self.grilla.EnableDragColMove( False )
		self.grilla.EnableDragColSize( True )
		self.grilla.SetColLabelSize( 30 )
		self.grilla.SetColLabelValue( 0, u"Código" )
		self.grilla.SetColLabelValue( 1, u"Apellido y nombre" )
		self.grilla.SetColLabelValue( 2, u"Sección" )
		self.grilla.SetColLabelValue( 3, u"Teléfono" )
		self.grilla.SetColLabelValue( 4, u"Camp" )
		self.grilla.SetColLabelValue( 5, u"Deuda" )
		self.grilla.SetColLabelValue( 6, u"Barrio" )
		self.grilla.SetColLabelValue( 7, u"Localidad" )
		self.grilla.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grilla.AutoSizeRows()
		self.grilla.EnableDragRowSize( True )
		self.grilla.SetRowLabelSize( 50 )
		self.grilla.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grilla.SetDefaultCellFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.grilla.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		sbSizer1.Add( self.grilla, 0, wx.ALL, 5 )
		
		gbSizer1.Add( sbSizer1, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 20 )
		
		self.btn_volver = wx.Button( self, wx.ID_CANCEL, u"Volver", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_volver.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_volver, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.LEFT, 20 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

