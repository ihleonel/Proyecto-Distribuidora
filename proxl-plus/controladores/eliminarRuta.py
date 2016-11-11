# -*- coding: utf-8 -*-
import wx
from vistas.frame_eliminar_ruta import Frame

from modelos.modelRutas import ModeloRutas

class ControladorEliminarRuta:
	mdlRutas = ModeloRutas()
	def __init__(self, parent, idRuta):
		self.parent = parent
		self.idRuta = idRuta

	def run(self):
		self.frame = Frame(self.parent)
		self.cargarDatos()
		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.Eliminar()

	def cargarDatos(self):
		self.mdlRutas.rut_id = self.idRuta
		datosRuta = self.mdlRutas.read()
		self.frame.tc_nombre.SetValue(datosRuta[0][1])
		self.frame.tc_orden.SetValue(str(datosRuta[0][2]))

	def Eliminar(self):
		self.mdlRutas.delete()