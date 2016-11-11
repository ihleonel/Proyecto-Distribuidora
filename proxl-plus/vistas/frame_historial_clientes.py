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
## Class FrameHistorialClientes
###########################################################################

class FrameHistorialClientes ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Historial de clientes", pos = wx.DefaultPosition, size = wx.Size( 1259,602 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Datos de busqueda" ), wx.VERTICAL )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Codigo:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gbSizer2.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_codigo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		gbSizer2.Add( self.tc_codigo, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Rango de campañas:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gbSizer2.Add( self.m_staticText2, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_rango = wx.TextCtrl( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE )
		self.tc_rango.SetMaxLength( 2 ) 
		gbSizer2.Add( self.tc_rango, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn_buscar = wx.Button( self, wx.ID_OK, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.btn_buscar, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.grilla = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 1190,400 ), 0 )
		
		# Grid
		self.grilla.CreateGrid( 0, 25 )
		self.grilla.EnableEditing( True )
		self.grilla.EnableGridLines( True )
		self.grilla.EnableDragGridSize( False )
		self.grilla.SetMargins( 0, 0 )
		
		# Columns
		self.grilla.SetColSize( 0, 80 )
		self.grilla.SetColSize( 1, 220 )
		self.grilla.SetColSize( 2, 50 )
		self.grilla.SetColSize( 3, 180 )
		self.grilla.SetColSize( 4, 180 )
		self.grilla.EnableDragColMove( False )
		self.grilla.EnableDragColSize( True )
		self.grilla.SetColLabelSize( 30 )
		self.grilla.SetColLabelValue( 0, u"Código" )
		self.grilla.SetColLabelValue( 1, u"Apellido y nombre" )
		self.grilla.SetColLabelValue( 2, u"Sección" )
		self.grilla.SetColLabelValue( 3, u"Domicilio" )
		self.grilla.SetColLabelValue( 4, u"Barrio" )
		self.grilla.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grilla.EnableDragRowSize( True )
		self.grilla.SetRowLabelSize( 80 )
		self.grilla.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grilla.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		gbSizer2.Add( self.grilla, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 5 ), wx.ALL, 5 )
		
		sbSizer1.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		gbSizer1.Add( sbSizer1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.TOP|wx.LEFT, 20 )
		
		self.btn_salir = wx.Button( self, wx.ID_ANY, u"Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.btn_salir, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.LEFT, 20 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

