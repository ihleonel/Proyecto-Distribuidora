# -*- coding: utf-8 -*-
import wx
from vistas.frame_modificar_ruta import Frame

from modelos.modelRutas import ModeloRutas

from validadores.validarNumerico import ValidarEntero
from validadores.validarNoVacio import NoVacio

class ControladorModificarRuta:
	mdlRutas = ModeloRutas()
	def __init__(self, parent, idRuta):
		self.parent = parent
		self.idRuta = idRuta

	def run(self):
		self.frame = Frame(self.parent)
		self.cargarDatos()
		self.cargarValidadores()
		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.Modificar()

	def cargarDatos(self):
		self.mdlRutas.rut_id = self.idRuta
		datosRuta = self.mdlRutas.read()
		self.frame.tc_nombre.SetValue(datosRuta[0][1])
		self.frame.tc_orden.SetValue(str(datosRuta[0][2]))


	def cargarValidadores(self):
		self.frame.tc_nombre.SetValidator(NoVacio())
		self.frame.tc_orden.SetValidator(ValidarEntero())

	def Modificar(self):
		self.mdlRutas.rut_nombre = self.frame.tc_nombre.GetValue().upper()
		self.mdlRutas.rut_orden = int(self.frame.tc_orden.GetValue())
		self.mdlRutas.update()