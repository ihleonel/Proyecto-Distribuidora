# -*- coding: utf-8 -*-
import wx
from datetime import datetime
from vistas.frame_modificar_gasto import FrameModificarGasto 
from validadores.validarNumerico import ValidarFlotante
from modelos.modelGastos import ModeloGastosVarios 

class ControladorModificarGasto:
	mdlGVar = ModeloGastosVarios()
	def __init__(self, parent, gasto):
		self.parent = parent 
		self.gasto = gasto

	def run(self):
		self.frame = FrameModificarGasto(self.parent)
		self.cargarValidadores()
		self.cargarDatos()
		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.Modificar()

	def cargarDatos(self):
		titulo = str(self.gasto['numero']) +'-'+str(self.gasto['anio'])
		self.frame.st_campania.SetLabel(titulo)
		self.frame.tc_fecha.SetValue(self.gasto['gast_fecha'])
		self.frame.tc_monto.SetValue(str(self.gasto['gast_monto']))
		self.frame.tc_concepto.SetValue(self.gasto['gast_concepto'])

	def cargarValidadores(self):
		self.frame.tc_monto.SetValidator(ValidarFlotante())

	def Modificar(self):
		self.mdlGVar.icam_anio = self.gasto['anio']
		self.mdlGVar.icam_num = self.gasto['numero']
		self.mdlGVar.i_numero = self.gasto['gast_num']
		self.mdlGVar.i_fecha = self.frame.tc_fecha.GetValue()
		self.mdlGVar.i_monto = float(self.frame.tc_monto.GetValue())
		self.mdlGVar.i_concepto = self.frame.tc_concepto.GetValue()
		
		self.mdlGVar.update()