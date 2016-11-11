# -*- coding: utf-8 -*-
import wx
from vistas.frame_eliminar_gasto import FrameEliminarGasto
from modelos.modelGastos import ModeloGastosVarios

class ControladorEliminarGasto:
	mdlEnv = ModeloGastosVarios()
	def __init__(self, parent, gasto):
		self.parent = parent
		self.gasto = gasto

	def run(self):
		self.frame = FrameEliminarGasto(self.parent)
		self.frame.tc_monto.SetFocus()
		self.cargarDatos()
		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.Eliminar()


	def cargarDatos(self):
		titulo = str(self.gasto['numero']) +'-'+str(self.gasto['anio'])
		self.frame.st_campania.SetLabel(titulo)
		self.frame.tc_fecha.SetValue(self.gasto['gast_fecha'])
		self.frame.tc_monto.SetValue(str(self.gasto['gast_monto']))
		self.frame.tc_concepto.SetValue(self.gasto['gast_concepto'])

	def Eliminar(self):
		self.mdlEnv.icam_anio =  int(self.gasto['anio'])
		self.mdlEnv.icam_num = int(self.gasto['numero'])
		self.mdlEnv.i_numero = int(self.gasto['gast_num'])

		self.mdlEnv.delete()