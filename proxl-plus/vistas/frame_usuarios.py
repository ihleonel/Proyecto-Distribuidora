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
## Class FrameUsuarios
###########################################################################

class FrameUsuarios ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Usuarios", pos = wx.DefaultPosition, size = wx.Size( 632,396 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Usuario:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.tc_usuario = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 270,-1 ), 0 )
		self.tc_usuario.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1.Add( self.tc_usuario, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btn_buscar = wx.Button( self, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_buscar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1.Add( self.btn_buscar, 0, wx.ALL, 5 )
		
		sbSizer1.Add( bSizer1, 1, wx.EXPAND, 5 )
		
		gbSizer1.Add( sbSizer1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.TOP|wx.LEFT, 20 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.grilla = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 450,150 ), 0 )
		
		# Grid
		self.grilla.CreateGrid( 0, 2 )
		self.grilla.EnableEditing( False )
		self.grilla.EnableGridLines( True )
		self.grilla.EnableDragGridSize( False )
		self.grilla.SetMargins( 0, 0 )
		
		# Columns
		self.grilla.SetColSize( 0, 200 )
		self.grilla.SetColSize( 1, 200 )
		self.grilla.EnableDragColMove( False )
		self.grilla.EnableDragColSize( False )
		self.grilla.SetColLabelSize( 30 )
		self.grilla.SetColLabelValue( 0, u"Usuario" )
		self.grilla.SetColLabelValue( 1, u"Tipo" )
		self.grilla.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grilla.AutoSizeRows()
		self.grilla.EnableDragRowSize( False )
		self.grilla.SetRowLabelSize( 30 )
		self.grilla.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grilla.SetDefaultCellFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.grilla.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.grilla.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.grilla, wx.GBPosition( 0, 0 ), wx.GBSpan( 4, 1 ), wx.ALL, 5 )
		
		self.btn_agregar = wx.Button( self, wx.ID_ANY, u"Agregar", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_agregar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.btn_agregar, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btn_modificar = wx.Button( self, wx.ID_ANY, u"Modificar", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_modificar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.btn_modificar.Enable( False )
		
		gbSizer2.Add( self.btn_modificar, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btn_ver = wx.Button( self, wx.ID_ANY, u"Ver", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_ver.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.btn_ver.Enable( False )
		
		gbSizer2.Add( self.btn_ver, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btn_eliminar = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_eliminar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.btn_eliminar.Enable( False )
		
		gbSizer2.Add( self.btn_eliminar, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_BOTTOM|wx.TOP|wx.ALIGN_CENTER_HORIZONTAL, 40 )
		
		sbSizer2.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		gbSizer1.Add( sbSizer2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.TOP|wx.LEFT, 20 )
		
		self.btn_volver = wx.Button( self, wx.ID_ANY, u"Volver ", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_volver.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_volver, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM|wx.LEFT, 20 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

