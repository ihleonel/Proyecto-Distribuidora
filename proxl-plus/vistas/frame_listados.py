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
## Class FrameListados
###########################################################################

class FrameListados ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Listados de campaña", pos = wx.DefaultPosition, size = wx.Size( 886,367 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Campaña:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		sbSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.st_campania = wx.StaticText( self, wx.ID_ANY, u"0000-00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.st_campania.Wrap( -1 )
		self.st_campania.SetFont( wx.Font( 13, 70, 90, 92, False, wx.EmptyString ) )
		
		sbSizer1.Add( self.st_campania, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		gbSizer1.Add( sbSizer1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.TOP|wx.LEFT, 20 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.grilla = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,155 ), 0 )
		
		# Grid
		self.grilla.CreateGrid( 0, 3 )
		self.grilla.EnableEditing( False )
		self.grilla.EnableGridLines( True )
		self.grilla.EnableDragGridSize( False )
		self.grilla.SetMargins( 0, 0 )
		
		# Columns
		self.grilla.SetColSize( 0, 120 )
		self.grilla.SetColSize( 1, 100 )
		self.grilla.SetColSize( 2, 390 )
		self.grilla.EnableDragColMove( True )
		self.grilla.EnableDragColSize( True )
		self.grilla.SetColLabelSize( 30 )
		self.grilla.SetColLabelValue( 0, u"Fecha" )
		self.grilla.SetColLabelValue( 1, u"Número" )
		self.grilla.SetColLabelValue( 2, u"Comentario" )
		self.grilla.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grilla.AutoSizeRows()
		self.grilla.EnableDragRowSize( True )
		self.grilla.SetRowLabelSize( 80 )
		self.grilla.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.grilla.SetLabelFont( wx.Font( 11, 70, 90, 92, False, wx.EmptyString ) )
		
		# Cell Defaults
		self.grilla.SetDefaultCellFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.grilla.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_TOP )
		gbSizer2.Add( self.grilla, wx.GBPosition( 0, 0 ), wx.GBSpan( 4, 1 ), wx.ALL, 5 )
		
		self.btn_agregar = wx.Button( self, wx.ID_ANY, u"Agregar", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_agregar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer2.Add( self.btn_agregar, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btn_modificar = wx.Button( self, wx.ID_ANY, u"Modificar", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_modificar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.btn_modificar.Enable( False )
		
		gbSizer2.Add( self.btn_modificar, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btn_eliminar = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_eliminar.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		self.btn_eliminar.Enable( False )
		
		gbSizer2.Add( self.btn_eliminar, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 20 )
		
		sbSizer2.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		gbSizer1.Add( sbSizer2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.TOP|wx.LEFT, 20 )
		
		self.btn_volver = wx.Button( self, wx.ID_CANCEL, u"Volver", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.btn_volver.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.btn_volver, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.TOP|wx.LEFT, 20 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

