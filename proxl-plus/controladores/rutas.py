# -*- coding: utf-8 -*-
import wx
from vistas.frame_rutas import Frame
from modelos.modelRutas import ModeloRutas

from controladores.agregarRuta import ControladorAgregarRuta
from controladores.modificarRuta import ControladorModificarRuta
from controladores.eliminarRuta import ControladorEliminarRuta

class ControladorRutas:
	mdlRutas = ModeloRutas()
	def __init__(self, parent):
		self.parent = parent

	def run(self):
		self.frame = Frame(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		self.cargarDatos()
		self.capturarEventos()
		self.frame.Show()

	def capturarEventos(self):
		self.frame.btn_agregar.Bind(wx.EVT_BUTTON, self.Agregar)
		self.frame.btn_modificar.Bind(wx.EVT_BUTTON, self.Modificar)
		self.frame.btn_eliminar.Bind(wx.EVT_BUTTON, self.Eliminar)
		self.frame.btn_salir.Bind(wx.EVT_BUTTON, self.Salir)
		self.frame.grilla.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.f_seleccion_fila)

	def configurar_grilla(self, tam):
		self.frame.grilla.SetSelectionMode(wx.grid.Grid.SelectRows)
		self.frame.grilla.AppendRows(tam)
		for i in range(tam):
			self.frame.grilla.SetRowSize(i, 25)
		
	def cargarDatos(self):
		self.listadoClientes = self.mdlRutas.read_all()

		if len(self.listadoClientes) != 0:
			self.cargarGrilla(self.listadoClientes)

	def cargarGrilla(self, listado):
		self.configurar_grilla(len(listado))
		for i in range(len(listado)):
			self.frame.grilla.SetRowLabelValue(i, "")
			self.frame.grilla.SetCellValue(i, 0, str(listado[i][0]))
			self.frame.grilla.SetCellValue(i, 1, listado[i][1])
			self.frame.grilla.SetCellValue(i, 2, str(listado[i][2]))

	def limpiar_grilla(self):
		for i in range(self.frame.grilla.GetNumberRows()):
			self.frame.grilla.DeleteRows(0, 1)

	def refrescar_grilla(self):
		self.limpiar_grilla()
		self.listadoClientes = self.mdlRutas.read_all()
		self.cargarGrilla(self.listadoClientes)

	# Eventos de la ventana.

	def Salir(self, event):
		self.frame.Destroy()

	def Agregar(self, event):
		agreRuta = ControladorAgregarRuta(self.frame)
		agreRuta.run()
		self.refrescar_grilla()
		self.DeshabilitarBTNS()

	def Modificar(self, event):
		modRuta = ControladorModificarRuta(self.frame, self.IdRuta)
		modRuta.run()
		self.refrescar_grilla()
		self.DeshabilitarBTNS()

	def Eliminar(self, event):
		eliRuta = ControladorEliminarRuta(self.frame, self.IdRuta)
		eliRuta.run()
		self.refrescar_grilla()
		self.DeshabilitarBTNS()

	# Eventos de grilla.

	def f_seleccion_fila(self, event):
		fila = event.GetRow()
		try:
			self.IdRuta = int(self.frame.grilla.GetCellValue(fila, 0))
			self.HabilitarBTNS()
		except:
			pass
		event.Skip()

	# Habilitacion Deshabilitacion.

	def HabilitarBTNS(self):
		self.frame.btn_modificar.Enable(True)
		self.frame.btn_eliminar.Enable(True)

	def DeshabilitarBTNS(self):
		self.frame.btn_modificar.Enable(False)
		self.frame.btn_eliminar.Enable(False)
	