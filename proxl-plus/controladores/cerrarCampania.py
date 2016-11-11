# -*- coding : utf-8 -*-
import wx
import time
from vistas.frame_cerrar_campania import FrameCerrarCampania

from modelos.modelCampanias import ModeloCampanias

class ControladorCerrarCampania:
	mdlCamp = ModeloCampanias()
	def __init__(self, parent, camp):
		self.parent = parent
		self.camp = camp

	def run(self):
		self.frame = FrameCerrarCampania(self.parent)
		self.frame.btn_cancelar.SetFocus()
		self.cargarDatos()
		rta = self.frame.ShowModal()

		if rta == wx.ID_OK:
			self.CerrarCampania()

		self.frame.Destroy()

	def cargarDatos(self):
		texto = str(self.camp['numero'])+'-'+str(self.camp['anio'])
		self.frame.st_campania.SetLabel(texto)
		self.frame.tc_inicio.SetValue(str(self.camp['inicio']))
		self.frame.tc_cierre.SetValue(time.strftime("%d-%m-%Y"))


	def CerrarCampania(self):
		self.mdlCamp.anio = self.camp['anio']
		self.mdlCamp.num = self.camp['numero']
		self.mdlCamp.fin = time.strftime("%Y-%m-%d")
		self.mdlCamp.close()