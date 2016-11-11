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
## Class PanelDos
###########################################################################

class PanelDos ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.btn_campanias = wx.Button( self, wx.ID_ANY, u"Campañas", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_campanias.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.btn_campanias, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btn_usuarios = wx.Button( self, wx.ID_ANY, u"Usuarios", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_usuarios.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.btn_usuarios, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btn_clientes = wx.Button( self, wx.ID_ANY, u"Clientes", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_clientes.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.btn_clientes, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btn_rutas = wx.Button( self, wx.ID_ANY, u"Rutas", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_rutas.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.btn_rutas, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		sbSizer1.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		gbSizer1.Add( sbSizer1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.TOP|wx.LEFT, 10 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Reportes" ), wx.VERTICAL )
		
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.btn_historial = wx.Button( self, wx.ID_ANY, u"Historial de Clientes", wx.DefaultPosition, wx.Size( 160,30 ), 0 )
		self.btn_historial.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer3.Add( self.btn_historial, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		sbSizer2.Add( gbSizer3, 1, wx.EXPAND, 5 )
		
		gbSizer1.Add( sbSizer2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.TOP|wx.LEFT, 10 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
	
	def __del__( self ):
		pass
	

