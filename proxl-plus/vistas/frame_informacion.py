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
## Class FrameInformacion
###########################################################################

class FrameInformacion ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Información de cliente", pos = wx.DefaultPosition, size = wx.Size( 771,378 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.btn_editar = wx.Button( self, wx.ID_ANY, u"Editar cliente", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.btn_editar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_editar, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.LEFT, 20 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Código:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Apellido y nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_staticText2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Zona:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_staticText3, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Campaña:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_staticText4, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Deuda:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.m_staticText5, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.tc_codigo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
		self.tc_codigo.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.tc_codigo.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		self.tc_codigo.SetMinSize( wx.Size( 70,-1 ) )
		
		gbSizer2.Add( self.tc_codigo, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.tc_apenom = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), wx.TE_READONLY )
		self.tc_apenom.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.tc_apenom.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		
		gbSizer2.Add( self.tc_apenom, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.tc_zona = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
		self.tc_zona.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.tc_zona.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		self.tc_zona.SetMinSize( wx.Size( 50,-1 ) )
		
		gbSizer2.Add( self.tc_zona, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.tc_campania = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
		self.tc_campania.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.tc_campania.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		self.tc_campania.SetMinSize( wx.Size( 70,-1 ) )
		
		gbSizer2.Add( self.tc_campania, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.tc_deuda = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		self.tc_deuda.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.tc_deuda, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cb_entregado = wx.CheckBox( self, wx.ID_ANY, u"Entregado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_entregado.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer3.Add( self.cb_entregado, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.rb_efectivo = wx.RadioButton( self, wx.ID_ANY, u"Efectivo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rb_efectivo.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer3.Add( self.rb_efectivo, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.rb_boleta = wx.RadioButton( self, wx.ID_ANY, u"Boleta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rb_boleta.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer3.Add( self.rb_boleta, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.rb_oficina = wx.RadioButton( self, wx.ID_ANY, u"Oficina", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rb_oficina.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer3.Add( self.rb_oficina, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.tc_entregado = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
		self.tc_entregado.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.tc_entregado.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		
		gbSizer3.Add( self.tc_entregado, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sbSizer2.Add( gbSizer3, 1, wx.EXPAND, 5 )
		
		gbSizer2.Add( sbSizer2, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		rb_rebotesChoices = [ u"Ninguno", u"A", u"S/B", u"R/D", u"ADC", u"Otros" ]
		self.rb_rebotes = wx.RadioBox( self, wx.ID_ANY, u"Rebote", wx.DefaultPosition, wx.DefaultSize, rb_rebotesChoices, 1, wx.RA_SPECIFY_ROWS )
		self.rb_rebotes.SetSelection( 0 )
		gbSizer2.Add( self.rb_rebotes, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.tc_otros = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,-1 ), 0 )
		self.tc_otros.SetMaxLength( 50 ) 
		self.tc_otros.Enable( False )
		
		gbSizer2.Add( self.tc_otros, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		sbSizer1.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		gbSizer1.Add( sbSizer1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 6 ), wx.EXPAND|wx.LEFT, 20 )
		
		self.btn_aceptar = wx.Button( self, wx.ID_OK, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_aceptar.SetFont( wx.Font( 11, 70, 90, 92, False, wx.EmptyString ) )
		self.btn_aceptar.SetMinSize( wx.Size( 100,30 ) )
		
		gbSizer1.Add( self.btn_aceptar, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btn_cancelar = wx.Button( self, wx.ID_CANCEL, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_cancelar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.btn_cancelar.SetMinSize( wx.Size( 100,30 ) )
		
		gbSizer1.Add( self.btn_cancelar, wx.GBPosition( 2, 5 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

