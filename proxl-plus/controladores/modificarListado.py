# -*- coding: utf-8 -*-
import wx

from vistas.frame_modificar_listado import FrameModificarListado 
from modelos.modelListados import ModeloListados

class ControladorModificarListado:
	mdlList = ModeloListados()

	def __init__(self, parent, camp, numLis):
		self.parent = parent
		self.camp = camp
		self.numLis = numLis

	def run(self):
		self.frame = FrameModificarListado(self.parent)
		self.frame.btn_cancelar.SetFocus()
		self.cargarDatos()
		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.Modificar()

	def cargarDatos(self):
		self.mdlList.cam_anio = self.camp['anio']
		self.mdlList.cam_num = self.camp['numero']
		self.mdlList.numero = self.numLis
		datos = self.mdlList.read()
		t = str(self.camp['anio']) +'-'+str(self.camp['numero'])
		self.frame.tc_campania.SetValue(t)
		self.frame.tc_fecha.SetValue(str(datos['fecha']))
		self.frame.tc_num_listado.SetValue(str(self.numLis))
		self.frame.tc_comentarios.SetValue(str(datos['comentario']))

	def Modificar(self):
		self.mdlList.cam_anio = self.camp['anio']
		self.mdlList.cam_num = self.camp['numero']
		self.mdlList.numero = self.numLis
		self.mdlList.comentario = self.frame.tc_comentarios.GetValue()
		self.mdlList.update()
