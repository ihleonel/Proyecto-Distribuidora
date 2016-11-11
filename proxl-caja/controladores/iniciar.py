# -*- coding: utf-8 -*-
import wx, time
from vistas.frame_iniciar_caja import FrameIniciarCaja
from modelos.modelCajas import ModeloCajas

class ControladorIniciarCaja:
	mdlCaj = ModeloCajas()
	def __init__(self, parent, datosCamp):
		self.parent = parent
		self.datosCamp = datosCamp

	def run(self):
		self.frame = FrameIniciarCaja(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		self.cargarDatos()
		resp = self.frame.ShowModal()
		if resp == wx.ID_OK:
			self.IniciarCaja()

	def cargarDatos(self):
		camp = str(self.datosCamp['anio']) + '-' + str(self.datosCamp['numero'])
		self.frame.st_campania.SetLabel(camp)
		self.frame.st_fecha_camp.SetLabel(self.datosCamp['inicio'])
		self.frame.st_fecha_caja.SetLabel(time.strftime("%d-%m-%Y"))
		self.mdlCaj.ccam_anio = self.datosCamp['anio']
		self.mdlCaj.ccam_num = self.datosCamp['numero']
		self.nCaja = self.mdlCaj.count_boxes() + 1
		self.frame.st_num_caja.SetLabel(str(self.nCaja))


	def IniciarCaja(self):
		self.mdlCaj.caj_numero = self.nCaja
		self.mdlCaj.caj_fecha = time.strftime("%Y-%m-%d")
		self.mdlCaj.caj_inicial = float(self.frame.tc_monto.GetValue())
		self.mdlCaj.create()