# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class FrameClientes
###########################################################################

class FrameClientes ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"CLIENTE", pos = wx.DefaultPosition, size = wx.Size( 1003,439 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Búsqueda" ), wx.VERTICAL )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.tc_dato_busqueda = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TE_PROCESS_ENTER )
		self.tc_dato_busqueda.SetMaxLength( 150 ) 
		self.tc_dato_busqueda.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.tc_dato_busqueda, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn_buscar = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_buscar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.btn_buscar, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		rbx_tipo_busquedaChoices = [ u"Por Código", u"Por Apellido y Nombre" ]
		self.rbx_tipo_busqueda = wx.RadioBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, rbx_tipo_busquedaChoices, 1, wx.RA_SPECIFY_ROWS )
		self.rbx_tipo_busqueda.SetSelection( 0 )
		self.rbx_tipo_busqueda.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.rbx_tipo_busqueda, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.LEFT, 5 )
		
		sbSizer1.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		gbSizer1.Add( sbSizer1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.TOP|wx.LEFT, 20 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Resultados" ), wx.VERTICAL )
		
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.grilla = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 510,120 ), 0 )
		
		# Grid
		self.grilla.CreateGrid( 0, 3 )
		self.grilla.EnableEditing( False )
		self.grilla.EnableGridLines( True )
		self.grilla.EnableDragGridSize( False )
		self.grilla.SetMargins( 0, 0 )
		
		# Columns
		self.grilla.SetColSize( 0, 80 )
		self.grilla.SetColSize( 1, 185 )
		self.grilla.SetColSize( 2, 182 )
		self.grilla.EnableDragColMove( False )
		self.grilla.EnableDragColSize( True )
		self.grilla.SetColLabelSize( 30 )
		self.grilla.SetColLabelValue( 0, u"Código" )
		self.grilla.SetColLabelValue( 1, u"Apellido y Nombre" )
		self.grilla.SetColLabelValue( 2, u"Domicilio" )
		self.grilla.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grilla.EnableDragRowSize( True )
		self.grilla.SetRowLabelSize( 50 )
		self.grilla.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grilla.SetDefaultCellFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.grilla.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.grilla.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer3.Add( self.grilla, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btn_seleccionar = wx.Button( self, wx.ID_ANY, u"Seleccionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_seleccionar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.btn_seleccionar.Enable( False )
		
		gbSizer3.Add( self.btn_seleccionar, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		sbSizer2.Add( gbSizer3, 1, wx.EXPAND, 5 )
		
		gbSizer1.Add( sbSizer2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.TOP|wx.LEFT, 20 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Movimiento" ), wx.VERTICAL )
		
		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Código:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		
		gbSizer4.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.tc_codigo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_CENTRE|wx.TE_READONLY )
		self.tc_codigo.SetMaxLength( 10 ) 
		self.tc_codigo.SetFont( wx.Font( 11, 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer4.Add( self.tc_codigo, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Apellido y Nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		
		gbSizer4.Add( self.m_staticText5, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.tc_apenom = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), wx.TE_READONLY )
		self.tc_apenom.SetMaxLength( 150 ) 
		self.tc_apenom.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer4.Add( self.tc_apenom, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 2 ), wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Campaña:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		
		gbSizer4.Add( self.m_staticText6, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Deuda:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		
		gbSizer4.Add( self.m_staticText7, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Aproximado:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		self.m_staticText51.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		
		gbSizer4.Add( self.m_staticText51, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.RIGHT|wx.LEFT|wx.ALIGN_BOTTOM, 5 )
		
		self.tc_camp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
		self.tc_camp.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer4.Add( self.tc_camp, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.tc_deuda = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
		self.tc_deuda.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer4.Add( self.tc_deuda, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.tc_aproximado = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
		self.tc_aproximado.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer4.Add( self.tc_aproximado, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer4.Add( self.m_staticline1, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 3 ), wx.EXPAND |wx.ALL, 5 )
		
		self.cb_entregado = wx.CheckBox( self, wx.ID_ANY, u"Entregado", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_entregado.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer4.Add( self.cb_entregado, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer4.Add( self.m_staticline2, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 3 ), wx.EXPAND |wx.ALL, 5 )
		
		self.rb_efectivo = wx.RadioButton( self, wx.ID_ANY, u"Efectivo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rb_efectivo.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer4.Add( self.rb_efectivo, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.tc_importe = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_PROCESS_ENTER )
		self.tc_importe.SetMaxLength( 10 ) 
		self.tc_importe.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.tc_importe.Enable( False )
		self.tc_importe.SetToolTipString( u"Importe Recibido" )
		
		gbSizer4.Add( self.tc_importe, wx.GBPosition( 10, 0 ), wx.GBSpan( 1, 1 ), wx.BOTTOM, 5 )
		
		self.tc_vuelto = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_READONLY )
		self.tc_vuelto.SetMaxLength( 10 ) 
		self.tc_vuelto.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.tc_vuelto.Enable( False )
		self.tc_vuelto.SetToolTipString( u"Vuelto a entregar" )
		
		gbSizer4.Add( self.tc_vuelto, wx.GBPosition( 11, 0 ), wx.GBSpan( 1, 1 ), wx.BOTTOM, 5 )
		
		self.rb_boleta = wx.RadioButton( self, wx.ID_ANY, u"Boleta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rb_boleta.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.rb_boleta.SetToolTipString( u"Centros de pago" )
		
		gbSizer4.Add( self.rb_boleta, wx.GBPosition( 9, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.rb_oficina = wx.RadioButton( self, wx.ID_ANY, u"Oficina", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rb_oficina.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.rb_oficina.SetToolTipString( u"Susana" )
		
		gbSizer4.Add( self.rb_oficina, wx.GBPosition( 9, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		sbSizer3.Add( gbSizer4, 1, wx.EXPAND, 5 )
		
		gbSizer1.Add( sbSizer3, wx.GBPosition( 0, 1 ), wx.GBSpan( 2, 4 ), wx.EXPAND|wx.TOP|wx.LEFT, 20 )
		
		self.btn_aceptar = wx.Button( self, wx.ID_OK, u"Aceptar", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_aceptar.SetFont( wx.Font( 11, 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_aceptar, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.btn_cancelar = wx.Button( self, wx.ID_CANCEL, u"Cancelar", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_cancelar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_cancelar, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

