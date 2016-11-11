# -*- coding:utf-8 -*-
import wx
from modelos.modelClientes import ModeloClientes
from vistas.frame_clientes import FrameClientes

from controladores.detalleCliente import ControladorDetalleCliente
from controladores.eliminarCliente import ControladorEliminarCliente
from controladores.agregarCliente import ControladorAgregarCliente
from controladores.modificarCliente import ControladorModificarCliente

class ControladorClientes:

	mdlCliente = ModeloClientes()

	def __init__(self, parent):
		self.parent = parent
		self.Seleccionado = None
		self.listadoClientes = None

	def run(self):
		self.frame = FrameClientes(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		self.capturarEventos()
		self.deshabilitarBTNS()
		self.frame.Show()

	def capturarEventos(self):
		self.frame.tc_dato_busqueda.Bind(wx.EVT_TEXT_ENTER, self.buscar)
		self.frame.tc_dato_busqueda.Bind(wx.EVT_TEXT, self.AutoCompletar)
		self.frame.btn_volver.Bind(wx.EVT_BUTTON, self.volver)
		self.frame.btn_buscar.Bind(wx.EVT_BUTTON, self.buscar)
		self.frame.btn_agregar.Bind(wx.EVT_BUTTON, self.agregar)
		self.frame.btn_modificar.Bind(wx.EVT_BUTTON, self.modificar)
		self.frame.btn_ver.Bind(wx.EVT_BUTTON, self.ver)
		self.frame.btn_eliminar.Bind(wx.EVT_BUTTON, self.eliminar)
		self.frame.grilla.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.f_seleccion_fila)
		self.frame.grilla.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.ver)

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
			self.frame.grilla.SetCellValue(i, 0, listado[i][0])
			self.frame.grilla.SetCellValue(i, 1, listado[i][1])
			self.frame.grilla.SetCellValue(i, 2, listado[i][2])

	def limpiar_grilla(self):
		for i in range(self.frame.grilla.GetNumberRows()):
			self.frame.grilla.DeleteRows(0, 1)

	def refrescar_grilla(self):
		self.limpiar_grilla()
		self.cargarGrilla(self.listadoClientes)

	'''Eventos de Botones'''
	def volver(self, event):
		self.mdlCliente.initialize()
		self.frame.Destroy()

	def agregar(self, event):
		agregar = ControladorAgregarCliente(self.frame)
		agregar.run()
		self.buscar()
		self.refrescar_grilla()
		self.deshabilitarBTNS()
		event.Skip()

	def modificar(self, event):
		modificar = ControladorModificarCliente(self.frame, self.Seleccionado)
		modificar.run()
		self.buscar()
		self.refrescar_grilla()
		self.deshabilitarBTNS()
		event.Skip()

	def ver(self, event):
		detalle = ControladorDetalleCliente(self.frame, self.Seleccionado)
		detalle.run()
		event.Skip()

	def eliminar(self, event):
		eliminar = ControladorEliminarCliente(self.frame, self.Seleccionado)
		eliminar.run()
		self.buscar()
		self.refrescar_grilla()
		self.deshabilitarBTNS()
		event.Skip()

	def buscar(self, event = None):
		if self.frame.tc_dato_busqueda.GetValue() != "":
			if self.frame.rb_codigo.GetValue():
				self.mdlCliente.apenom = ""
				self.mdlCliente.codigo = self.frame.tc_dato_busqueda.GetValue()
				self.listadoClientes = self.mdlCliente.read_all_for_code()
			else:
				self.mdlCliente.codigo = ""
				self.mdlCliente.apenom = self.frame.tc_dato_busqueda.GetValue()
				self.listadoClientes = self.mdlCliente.read_all_for_name()

			self.refrescar_grilla()
			self.Seleccionado = None
			self.deshabilitarBTNS()
		if event != None:
			event.Skip()

	def AutoCompletar(self, event):
		if self.frame.rb_codigo.GetValue():
			prefijo = self.frame.tc_dato_busqueda.GetValue()
			if len(prefijo) == 4:
				sufijo = prefijo[-1]
				if sufijo != "/": 
					prefijo = prefijo[:3] + "/"
					prefijo += sufijo
					self.frame.tc_dato_busqueda.SetValue(prefijo)
			self.frame.tc_dato_busqueda.SetInsertionPoint(len(prefijo))
		event.Skip()

	'''Eventos de Grilla'''
	def f_seleccion_fila(self, event):
		fila = event.GetRow()
		try:
			self.Seleccionado = self.frame.grilla.GetCellValue(fila, 0)
			self.habilitarBTNS()
		except:
			pass
		event.Skip()

	'''Habilitaciones'''
	def deshabilitarBTNS(self):
		self.frame.btn_modificar.Enable(False)
		self.frame.btn_ver.Enable(False)
		self.frame.btn_eliminar.Enable(False)
		
	def habilitarBTNS(self):
		self.frame.btn_modificar.Enable(True)
		self.frame.btn_ver.Enable(True)
		self.frame.btn_eliminar.Enable(True)

