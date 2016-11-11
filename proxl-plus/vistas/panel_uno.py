# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class PanelUno
###########################################################################

class PanelUno ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 514,404 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.st_campania = wx.StaticText( self, wx.ID_ANY, u"0000-00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_campania.Wrap( -1 )
		self.st_campania.SetFont( wx.Font( 13, 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.st_campania, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_BOTTOM|wx.LEFT, 20 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Código de cliente:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_staticText2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.LEFT, 10 )
		
		self.tc_codigo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 270,-1 ), wx.TE_PROCESS_ENTER )
		self.tc_codigo.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.tc_codigo, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 10 )
		
		self.btn_buscar = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.Size( 270,30 ), 0 )
		self.btn_buscar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.btn_buscar, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.BOTTOM|wx.RIGHT|wx.LEFT, 10 )
		
		self.btn_resultados_campania = wx.Button( self, wx.ID_ANY, u"Resultados Parciales de Campaña", wx.DefaultPosition, wx.Size( 270,40 ), 0 )
		self.btn_resultados_campania.SetFont( wx.Font( 11, 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.btn_resultados_campania, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 120 )
		
		sbSizer1.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		gbSizer1.Add( sbSizer1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.TOP|wx.LEFT, 20 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.btn_crear_campania = wx.Button( self, wx.ID_ANY, u"Crear campaña", wx.DefaultPosition, wx.Size( 135,30 ), 0 )
		self.btn_crear_campania.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		sbSizer2.Add( self.btn_crear_campania, 0, wx.ALL, 10 )
		
		self.btn_cerrar_campania = wx.Button( self, wx.ID_ANY, u"Cerrar campaña", wx.DefaultPosition, wx.Size( 135,30 ), 0 )
		self.btn_cerrar_campania.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		sbSizer2.Add( self.btn_cerrar_campania, 0, wx.ALL, 10 )
		
		self.btn_modificar_campania = wx.Button( self, wx.ID_ANY, u"Modificar campaña", wx.DefaultPosition, wx.Size( 135,30 ), 0 )
		self.btn_modificar_campania.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		sbSizer2.Add( self.btn_modificar_campania, 0, wx.ALL, 10 )
		
		self.btn_listados = wx.Button( self, wx.ID_ANY, u"Listados", wx.DefaultPosition, wx.Size( 135,30 ), 0 )
		self.btn_listados.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		sbSizer2.Add( self.btn_listados, 0, wx.ALL, 10 )
		
		self.btn_repartos = wx.Button( self, wx.ID_ANY, u"Repartos", wx.DefaultPosition, wx.Size( 135,30 ), 0 )
		self.btn_repartos.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		sbSizer2.Add( self.btn_repartos, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btn_gastos = wx.Button( self, wx.ID_ANY, u"Gastos Varios", wx.DefaultPosition, wx.Size( 135,30 ), 0 )
		self.btn_gastos.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		sbSizer2.Add( self.btn_gastos, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )
		
		self.btn_depositos = wx.Button( self, wx.ID_ANY, u"Depositos", wx.DefaultPosition, wx.Size( 135,30 ), 0 )
		self.btn_depositos.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		sbSizer2.Add( self.btn_depositos, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gbSizer1.Add( sbSizer2, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.TOP, 20 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
	
	def __del__( self ):
		pass
	

