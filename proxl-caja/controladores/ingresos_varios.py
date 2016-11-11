# -*- coding: utf-8 -*-
import wx
from vistas.frame_caja_ingresos_varios import FrameCajaIngresosVarios

from validadores.validarOpCaja import Monto

from modelos.modelMovimientos import ModeloMovimientos

class ControladorCajaIngresosVarios:
	mdlMov = ModeloMovimientos()

	def __init__(self, parent, infoCaja):
		self.parent = parent
		self.infoCaja = infoCaja

	def run(self):
		self.frame = FrameCajaIngresosVarios(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		self.frame.tc_monto.SetValidator(Monto())
		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.Aceptar()

		

	def Aceptar(self):
		self.mdlMov.mcam_anio = self.infoCaja['campAnio']
		self.mdlMov.mcam_num = self.infoCaja['campNum']
		self.mdlMov.mcaj_numero = self.infoCaja['numero']
		self.mdlMov.mov_numero = self.mdlMov.count_movs() + 1# numero de secuencia del siguiente movimiento
		self.mdlMov.mov_monto = float(self.frame.tc_monto.GetValue())
		self.mdlMov.mov_tipo = 1
		self.mdlMov.mov_comentario = self.frame.tc_comentario.GetValue()

		self.mdlMov.create()


