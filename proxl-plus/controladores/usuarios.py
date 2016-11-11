# -*- coding : utf-8 -*-
import wx

from vistas.frame_usuarios import FrameUsuarios
from controladores.agregarUsuario import ControladorAgregarUsuario
from controladores.modificarUsuario import ControladorModificarUsuario
from controladores.verUsuario import ControladorVerUsuario
from controladores.eliminarUsuario import ControladorEliminarUsuario
from modelos.modelUsuarios import ModeloUsuarios

class ControladorUsuarios:
	mdlUsu = ModeloUsuarios()
	def __init__(self, parent):
		self.parent = parent
		self.listadoUsuarios = self.mdlUsu.read_all()

	def run(self):
		self.frame = FrameUsuarios(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		self.capturarEventos()
		self.cargarGrilla(self.listadoUsuarios)
		self.deshabilitarBTNS()
		self.frame.Show()

	def capturarEventos(self):
		self.frame.btn_buscar.Bind(wx.EVT_BUTTON, self.Buscar)
		self.frame.btn_agregar.Bind(wx.EVT_BUTTON, self.Agregar)
		self.frame.btn_modificar.Bind(wx.EVT_BUTTON, self.Modificar)
		self.frame.btn_ver.Bind(wx.EVT_BUTTON, self.Ver)
		self.frame.btn_eliminar.Bind(wx.EVT_BUTTON, self.Eliminar)
		self.frame.btn_volver.Bind(wx.EVT_BUTTON, self.Volver)
		self.frame.grilla.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.f_seleccion_fila)
		self.frame.grilla.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.Ver)

	def configurar_grilla(self, tam):
		self.frame.grilla.SetSelectionMode(wx.grid.Grid.SelectRows)
		self.frame.grilla.AppendRows(tam)
		presentador = wx.grid.GridCellAutoWrapStringRenderer
		for i in range(tam):
			self.frame.grilla.SetRowSize(i, 25)
			self.frame.grilla.SetCellRenderer(i, 1, presentador())

	def cargarGrilla(self, listado):
		self.configurar_grilla(len(listado))
		for i in range(len(listado)):
			self.frame.grilla.SetCellValue(i, 0, listado[i]['usuario'])
			self.frame.grilla.SetCellValue(i, 1, listado[i]['tipo'])

	def limpiar_grilla(self):
		for i in range(self.frame.grilla.GetNumberRows()):
			self.frame.grilla.DeleteRows(0, 1)

	def refrescar_grilla(self):
		self.limpiar_grilla()
		self.cargarGrilla(self.listadoUsuarios)
		

	'''Eventos de botones'''
	def Buscar(self, event = None):
		if self.frame.tc_usuario.GetValue() != "":
			self.mdlUsu.usuario = self.frame.tc_usuario.GetValue()
			self.listadoUsuarios = self.mdlUsu.read_all_for_name()
			self.refrescar_grilla()
		else:
			self.listadoUsuarios = self.mdlUsu.read_all()
			self.refrescar_grilla()
		
		self.deshabilitarBTNS()

	def Agregar(self, event):
		addUser = ControladorAgregarUsuario(self.frame)
		addUser.run()
		self.listadoUsuarios = self.mdlUsu.read_all()
		self.refrescar_grilla()
		self.deshabilitarBTNS()

	def Modificar(self, event):
		updUser = ControladorModificarUsuario(self.frame, self.Seleccionado)
		updUser.run()
		self.listadoUsuarios = self.mdlUsu.read_all()
		self.refrescar_grilla()
		self.deshabilitarBTNS()

	def Ver(self, event):
		verUser = ControladorVerUsuario(self.frame, self.Seleccionado)
		verUser.run()

	def Eliminar(self, event):
		elimUser = ControladorEliminarUsuario(self.frame, self.Seleccionado)
		elimUser.run()
		self.listadoUsuarios = self.mdlUsu.read_all()
		self.refrescar_grilla()
		self.deshabilitarBTNS()

	def Volver(self, event):
		self.frame.Destroy()

	'''Eventos de grilla'''
	def f_seleccion_fila(self, event):
		fila = event.GetRow()
		try:
			self.Seleccionado = self.frame.grilla.GetCellValue(fila, 0)
			self.habilitarBTNS()
		except:
			pass
		event.Skip()

	def deshabilitarBTNS(self):
		self.frame.btn_modificar.Enable(False)
		self.frame.btn_ver.Enable(False)
		self.frame.btn_eliminar.Enable(False)
		
	def habilitarBTNS(self):
		self.frame.btn_modificar.Enable(True)
		self.frame.btn_ver.Enable(True)
		self.frame.btn_eliminar.Enable(True)

	'''Eventos de ventana'''
