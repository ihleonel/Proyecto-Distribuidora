# -*- coding: utf-8 -*-
import wx
from datetime import datetime
from vistas.frame_agregar_gasto import FrameAgregarGasto 
from validadores.validarNumerico import ValidarFlotante
from modelos.modelGastos import ModeloGastosVarios 

class ControladorAgregarGasto:
	mdlGVar = ModeloGastosVarios()
	def __init__(self, parent, camp):
		self.parent = parent 
		self.camp = camp

	def run(self):
		self.frame = FrameAgregarGasto(self.parent)
		self.frame.tc_monto.SetFocus()
		self.frame.tc_monto.SelectAll()
		self.cargarValidadores()
		self.cargarDatos()
		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.Agregar()

	def cargarDatos(self):
		titulo = str(self.camp['numero']) +'-'+str(self.camp['anio'])
		self.frame.st_campania.SetLabel(titulo)
		self.frame.tc_fecha.SetValue(datetime.today().strftime("%d-%m-%Y"))

	def cargarValidadores(self):
		self.frame.tc_monto.SetValidator(ValidarFlotante())

	def Agregar(self):
		self.mdlGVar.icam_anio = self.camp['anio']
		self.mdlGVar.icam_num = self.camp['numero']
		self.mdlGVar.i_numero = self.mdlGVar.last_spending() + 1
		self.mdlGVar.i_fecha = self.frame.tc_fecha.GetValue()
		self.mdlGVar.i_monto = float(self.frame.tc_monto.GetValue())
		self.mdlGVar.i_concepto = self.frame.tc_concepto.GetValue()

		self.mdlGVar.create()