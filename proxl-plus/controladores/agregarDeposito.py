# -*- coding: utf-8 -*-
import wx
from datetime import datetime
from vistas.frame_agregar_deposito import FrameAgregarDeposito
from modelos.modelEnvios import ModeloEnvios
from validadores.validarNumerico import ValidarFlotante 

class ControladorAgregarDeposito:
	mdlEnv = ModeloEnvios()
	def __init__(self, parent, camp):
		self.parent = parent
		self.camp = camp

	def run(self):
		self.frame = FrameAgregarDeposito(self.parent)
		self.frame.tc_monto.SetFocus()
		self.cargarValidadores()
		self.cargarDatos()
		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.Agregar()

	def cargarValidadores(self):
		self.frame.tc_monto.SetValidator(ValidarFlotante())


	def cargarDatos(self):
		titulo = str(self.camp['numero']) +'-'+str(self.camp['anio'])
		self.frame.st_campania.SetLabel(titulo)
		self.mdlEnv.ecam_anio = self.camp['anio']
		self.mdlEnv.ecam_num = self.camp['numero']
		numeroDep = self.mdlEnv.last_deposit() + 1
		self.frame.tc_numero.SetValue(str(numeroDep))
		self.frame.tc_fecha.SetValue(datetime.today().strftime("%d-%m-%Y"))

	def Agregar(self):
		self.mdlEnv.env_num = int(self.frame.tc_numero.GetValue())
		self.mdlEnv.env_monto = float(self.frame.tc_monto.GetValue())
		self.mdlEnv.env_fecha = self.frame.tc_fecha.GetValue()

		self.mdlEnv.create()