# -*- coding: utf-8 -*- 

import wx
import wx.xrc

###########################################################################
## Class FrameLogin
###########################################################################

class FrameLogin ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Se requiere autenticación", pos = wx.DefaultPosition, size = wx.Size( 449,191 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.Size( 449,191 ), wx.Size( -1,191 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.AddGrowableCol( 1 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Nombre de usuario", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_usuario = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tc_usuario.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.tc_usuario, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 10 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Contraseña", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.m_staticText2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_clave = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		self.tc_clave.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.tc_clave, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 10 )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btn_aceptar = wx.Button( self, wx.ID_OK, u"Aceptar", wx.DefaultPosition, wx.Size( 90,35 ), 0 )
		self.btn_aceptar.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1.Add( self.btn_aceptar, 0, wx.ALL, 10 )
		
		self.btn_cancelar = wx.Button( self, wx.ID_CANCEL, u"Cancelar", wx.DefaultPosition, wx.Size( 90,35 ), 0 )
		self.btn_cancelar.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1.Add( self.btn_cancelar, 0, wx.ALL, 10 )
		
		gbSizer1.Add( bSizer1, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

