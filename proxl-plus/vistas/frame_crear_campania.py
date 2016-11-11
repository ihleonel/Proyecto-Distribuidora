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
## Class FrameCrearCampania
###########################################################################

class FrameCrearCampania ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Iniciar Campaña", pos = wx.DefaultPosition, size = wx.Size( 648,438 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Fecha de Inicio:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_fecha_inicio = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
		self.tc_fecha_inicio.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.tc_fecha_inicio, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Número:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_staticText2, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.tc_numero = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE )
		self.tc_numero.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.tc_numero, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Usuario:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_staticText5, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.tc_usuario = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
		self.tc_usuario.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.tc_usuario, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer2.Add( self.m_staticline1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 6 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Inicio de Reparto:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		self.m_staticText51.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_staticText51, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_ini_reparto = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tc_ini_reparto.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.tc_ini_reparto.SetToolTipString( u"Fecha de inicio" )
		
		gbSizer2.Add( self.tc_ini_reparto, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Diferencia con anterior:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_staticText6, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.tc_diferencia = wx.TextCtrl( self, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		self.tc_diferencia.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.tc_diferencia.SetToolTipString( u"Diferencia en pesos" )
		
		gbSizer2.Add( self.tc_diferencia, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Distribución = (Pedidos a cobrar) x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer3.Add( self.m_staticText7, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_parametro = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_RIGHT )
		self.tc_parametro.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer3.Add( self.tc_parametro, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer3.Add( self.m_staticText8, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_base = wx.TextCtrl( self, wx.ID_ANY, u"7000.00", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		self.tc_base.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer3.Add( self.tc_base, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		sbSizer2.Add( gbSizer3, 1, wx.EXPAND, 5 )
		
		gbSizer2.Add( sbSizer2, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 6 ), wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Comentario:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_staticText3, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.tc_comentario = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,150 ), wx.TE_MULTILINE )
		self.tc_comentario.SetMaxLength( 700 ) 
		self.tc_comentario.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.tc_comentario, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 5 ), wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		sbSizer1.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		gbSizer1.Add( sbSizer1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 6 ), wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 20 )
		
		self.btn_cancelar = wx.Button( self, wx.ID_CANCEL, u"Cancelar", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_cancelar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_cancelar, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.LEFT, 10 )
		
		self.btn_aceptar = wx.Button( self, wx.ID_OK, u"Aceptar", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_aceptar.SetFont( wx.Font( 11, 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_aceptar, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

