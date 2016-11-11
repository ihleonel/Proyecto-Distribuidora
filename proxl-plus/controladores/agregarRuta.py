# -*- coding: utf-8 -*-
import wx
from vistas.frame_agregar_ruta import Frame

from modelos.modelRutas import ModeloRutas

from validadores.validarNumerico import ValidarEntero
from validadores.validarNoVacio import NoVacio

class ControladorAgregarRuta:
	mdlRutas = ModeloRutas()
	def __init__(self, parent):
		self.parent = parent

	def run(self):
		self.frame = Frame(self.parent)
		self.cargarValidadores()
		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.Aceptar()

	def cargarValidadores(self):
		self.frame.tc_nombre.SetValidator(NoVacio())
		self.frame.tc_orden.SetValidator(ValidarEntero())

	def Aceptar(self):
		self.mdlRutas.rut_nombre = self.frame.tc_nombre.GetValue().upper()
		self.mdlRutas.rut_orden = int(self.frame.tc_orden.GetValue())
		self.mdlRutas.create()