# -*- coding: utf-8 -*-
import wx
from vistas.frame_depositos import FrameDepositos
from controladores.agregarDeposito import ControladorAgregarDeposito
from controladores.modificarDeposito import ControladorModificarDeposito
from controladores.eliminarDeposito import ControladorEliminarDeposito
from modelos.modelEnvios import ModeloEnvios
class ControladorDepositos:
	mdlEnv = ModeloEnvios()

	def __init__(self, parent, camp):
		self.parent = parent
		self.camp = camp

	def run(self):
		self.frame = FrameDepositos(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
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
		self.mdlEnv.ecam_anio = self.camp['anio']
		self.mdlEnv.ecam_num = self.camp['numero']
		self.listadoEnv = self.mdlEnv.read_all()
		if self.listadoEnv != ():
			self.cargarGrilla(self.listadoEnv)

	def configurar_grilla(self, tam):
		self.frame.grilla.SetSelectionMode(wx.grid.Grid.SelectRows)
		self.frame.grilla.AppendRows(tam)
		for i in range(tam):
			self.frame.grilla.SetRowSize(i, 25)

	def cargarGrilla(self, listado):
		self.configurar_grilla(len(listado))
		for i in range(len(listado)):
			self.frame.grilla.SetCellValue(i, 0, str(listado[i][2]))
			self.frame.grilla.SetCellValue(i, 1, str(listado[i][3]))
			self.frame.grilla.SetCellValue(i, 2, str(listado[i][4]))

	def limpiar_grilla(self):
		for i in range(self.frame.grilla.GetNumberRows()):
			self.frame.grilla.DeleteRows(0, 1)

	def refrescar_grilla(self):
		self.limpiar_grilla()
		self.listadoEnv = self.mdlEnv.read_all()
		if self.listadoEnv != ():
			self.cargarGrilla(self.listadoEnv)

	"Eventos"
	def Agregar(self, event):
		agrDep = ControladorAgregarDeposito(self.frame, self.camp)
		agrDep.run()
		self.refrescar_grilla()
		self.DeshabilitarBTNS()

	def Modificar(self, event):
		modDep = ControladorModificarDeposito(self.frame, self.depos)
		modDep.run()
		self.refrescar_grilla()
		self.DeshabilitarBTNS()

	def Eliminar(self, event):
		eliDep = ControladorEliminarDeposito(self.frame, self.depos)
		eliDep.run()
		self.refrescar_grilla()
		self.DeshabilitarBTNS()

	"habilitar/desabilitar botones"

	def habilitarBTNS(self):
		self.frame.btn_modificar.Enable(True)
		self.frame.btn_eliminar.Enable(True)	

	def DeshabilitarBTNS(self):
		self.frame.btn_modificar.Enable(False)
		self.frame.btn_eliminar.Enable(False)

	def f_seleccion_fila(self, event):
		fila = event.GetRow()
		try:
			self.depos = {}
			self.depos['anio'] = self.camp['anio']
			self.depos['numero'] = self.camp['numero']
			self.depos['env_num'] = self.frame.grilla.GetCellValue(fila, 0)
			self.depos['env_fecha'] = self.frame.grilla.GetCellValue(fila, 1)
			self.depos['env_monto'] = self.frame.grilla.GetCellValue(fila, 2)
			self.habilitarBTNS()
		except:
			pass
		event.Skip()