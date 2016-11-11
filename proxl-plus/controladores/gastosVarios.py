# -*- coding: utf-8 -*-
import wx
from vistas.frame_gastos_varios import FrameGastosVarios
from controladores.agregarGasto import ControladorAgregarGasto
from controladores.modificarGasto import ControladorModificarGasto
from controladores.eliminarGasto import ControladorEliminarGasto
from modelos.modelGastos import ModeloGastosVarios
class ControladorGastosVarios:
	mdlGVar = ModeloGastosVarios()

	def __init__(self, parent, camp):
		self.parent = parent
		self.camp = camp

	def run(self):
		self.frame = FrameGastosVarios(self.parent)
		self.cargarDatos()
		self.capturarEventos()
		self.frame.Show()

	def capturarEventos(self):
		self.frame.btn_agregar.Bind(wx.EVT_BUTTON, self.Agregar)
		self.frame.btn_modificar.Bind(wx.EVT_BUTTON, self.Modificar)
		self.frame.btn_eliminar.Bind(wx.EVT_BUTTON, self.Eliminar)
		self.frame.grilla.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.f_seleccion_fila)

	def cargarDatos(self):
		titulo = str(self.camp['numero']) +'-'+str(self.camp['anio'])
		self.frame.st_campania.SetLabel(titulo)
		self.mdlGVar.icam_anio = self.camp['anio']
		self.mdlGVar.icam_num = self.camp['numero']
		self.listadoGastos = self.mdlGVar.read_all()
		if self.listadoGastos != ():
			self.cargarGrilla(self.listadoGastos)

	def configurar_grilla(self, tam):
		self.frame.grilla.SetSelectionMode(wx.grid.Grid.SelectRows)
		self.frame.grilla.AppendRows(tam)
		for i in range(tam):
			self.frame.grilla.SetRowSize(i, 25)

	def cargarGrilla(self, listado):
		self.configurar_grilla(len(listado))
		for i in range(len(listado)):
			self.frame.grilla.SetCellValue(i, 0, str(listado[i][3]))
			self.frame.grilla.SetCellValue(i, 1, str(listado[i][4]))
			self.frame.grilla.SetCellValue(i, 2, str(listado[i][5]))

	def limpiar_grilla(self):
		for i in range(self.frame.grilla.GetNumberRows()):
			self.frame.grilla.DeleteRows(0, 1)

	def refrescar_grilla(self):
		self.limpiar_grilla()
		self.listadoGastos = self.mdlGVar.read_all()
		if self.listadoGastos != ():
			self.cargarGrilla(self.listadoGastos)

	def Agregar(self, event):
		agr = ControladorAgregarGasto(self.frame, self.camp)
		agr.run()
		self.refrescar_grilla()

	def Modificar(self, event):
		mod = ControladorModificarGasto(self.parent, self.gasto)
		mod.run()
		self.refrescar_grilla()

	def Eliminar(self, event):
		elim = ControladorEliminarGasto(self.parent, self.gasto)
		elim.run()
		self.refrescar_grilla()

	def habilitarBTNS(self):
		self.frame.btn_modificar.Enable(True)
		self.frame.btn_eliminar.Enable(True)	

	def DeshabilitarBTNS(self):
		self.frame.btn_modificar.Enable(False)
		self.frame.btn_eliminar.Enable(False)

	def f_seleccion_fila(self, event):
		fila = event.GetRow()
		try:
			self.gasto = {}
			self.gasto['anio'] = self.camp['anio']
			self.gasto['numero'] = self.camp['numero']
			self.gasto['gast_num'] = self.listadoGastos[fila][2] # i_numero
			self.gasto['gast_fecha'] = self.listadoGastos[fila][3]
			self.gasto['gast_monto'] = self.listadoGastos[fila][4]
			self.gasto['gast_concepto'] = self.listadoGastos[fila][5]
			self.habilitarBTNS()
		except:
			pass
		event.Skip()