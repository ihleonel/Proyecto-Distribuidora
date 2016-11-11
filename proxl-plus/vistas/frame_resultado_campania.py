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
## Class FrameResultadoCampania
###########################################################################

class FrameResultadoCampania ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Resultados parciales de campaña", pos = wx.DefaultPosition, size = wx.Size( 893,507 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Campaña:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 20 )
		
		self.tc_campania = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tc_campania.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.tc_campania, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Inicio de campaña:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_staticText2, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.tc_inicio = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tc_inicio.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.tc_inicio, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn_generar = wx.Button( self, wx.ID_ANY, u"Generar Reporte", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_generar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_generar, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.LEFT, 20 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.grilla = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 820,190 ), 0 )
		
		# Grid
		self.grilla.CreateGrid( 6, 9 )
		self.grilla.EnableEditing( False )
		self.grilla.EnableGridLines( True )
		self.grilla.EnableDragGridSize( False )
		self.grilla.SetMargins( 0, 0 )
		
		# Columns
		self.grilla.SetColSize( 0, 170 )
		self.grilla.EnableDragColMove( False )
		self.grilla.EnableDragColSize( False )
		self.grilla.SetColLabelSize( 1 )
		self.grilla.SetColLabelValue( 0, wx.EmptyString )
		self.grilla.SetColLabelValue( 1, wx.EmptyString )
		self.grilla.SetColLabelValue( 2, wx.EmptyString )
		self.grilla.SetColLabelValue( 3, wx.EmptyString )
		self.grilla.SetColLabelValue( 4, wx.EmptyString )
		self.grilla.SetColLabelValue( 5, wx.EmptyString )
		self.grilla.SetColLabelValue( 6, wx.EmptyString )
		self.grilla.SetColLabelValue( 7, wx.EmptyString )
		self.grilla.SetColLabelValue( 8, wx.EmptyString )
		self.grilla.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grilla.SetRowSize( 0, 30 )
		self.grilla.SetRowSize( 1, 30 )
		self.grilla.SetRowSize( 2, 30 )
		self.grilla.SetRowSize( 3, 30 )
		self.grilla.SetRowSize( 4, 30 )
		self.grilla.SetRowSize( 5, 30 )
		self.grilla.EnableDragRowSize( False )
		self.grilla.SetRowLabelSize( 1 )
		self.grilla.SetRowLabelValue( 0, wx.EmptyString )
		self.grilla.SetRowLabelValue( 1, wx.EmptyString )
		self.grilla.SetRowLabelValue( 2, wx.EmptyString )
		self.grilla.SetRowLabelValue( 3, wx.EmptyString )
		self.grilla.SetRowLabelValue( 4, wx.EmptyString )
		self.grilla.SetRowLabelValue( 5, wx.EmptyString )
		self.grilla.SetRowLabelValue( 6, wx.EmptyString )
		self.grilla.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grilla.SetDefaultCellFont( wx.Font( 13, 70, 90, 90, False, wx.EmptyString ) )
		self.grilla.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		sbSizer1.Add( self.grilla, 0, wx.ALL, 5 )
		
		self.grilla2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grilla2.CreateGrid( 3, 4 )
		self.grilla2.EnableEditing( True )
		self.grilla2.EnableGridLines( True )
		self.grilla2.EnableDragGridSize( False )
		self.grilla2.SetMargins( 0, 0 )
		
		# Columns
		self.grilla2.SetColSize( 0, 170 )
		self.grilla2.SetColSize( 1, 130 )
		self.grilla2.SetColSize( 2, 130 )
		self.grilla2.SetColSize( 3, 130 )
		self.grilla2.EnableDragColMove( False )
		self.grilla2.EnableDragColSize( True )
		self.grilla2.SetColLabelSize( 1 )
		self.grilla2.SetColLabelValue( 0, wx.EmptyString )
		self.grilla2.SetColLabelValue( 1, wx.EmptyString )
		self.grilla2.SetColLabelValue( 2, wx.EmptyString )
		self.grilla2.SetColLabelValue( 3, wx.EmptyString )
		self.grilla2.SetColLabelValue( 4, wx.EmptyString )
		self.grilla2.SetColLabelValue( 5, wx.EmptyString )
		self.grilla2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grilla2.SetRowSize( 0, 30 )
		self.grilla2.SetRowSize( 1, 30 )
		self.grilla2.SetRowSize( 2, 30 )
		self.grilla2.EnableDragRowSize( True )
		self.grilla2.SetRowLabelSize( 1 )
		self.grilla2.SetRowLabelValue( 0, wx.EmptyString )
		self.grilla2.SetRowLabelValue( 1, wx.EmptyString )
		self.grilla2.SetRowLabelValue( 2, wx.EmptyString )
		self.grilla2.SetRowLabelValue( 3, wx.EmptyString )
		self.grilla2.SetRowLabelValue( 4, wx.EmptyString )
		self.grilla2.SetRowLabelValue( 5, wx.EmptyString )
		self.grilla2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grilla2.SetDefaultCellFont( wx.Font( 13, 70, 90, 90, False, wx.EmptyString ) )
		self.grilla2.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		sbSizer1.Add( self.grilla2, 0, wx.ALL, 5 )
		
		gbSizer1.Add( sbSizer1, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 4 ), wx.EXPAND|wx.LEFT, 20 )
		
		self.btn_volver = wx.Button( self, wx.ID_ANY, u"Volver", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_volver.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_volver, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 4 ), wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_RIGHT, 20 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

