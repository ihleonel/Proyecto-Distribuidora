# -*- coding: utf-8 -*-
import wx
import time
from modelos.modelClientes import ModeloClientes
from validadores.validarCliente import ValidarCodigo
from vistas.frame_agregar_cliente import FrameAgregarCliente

class ControladorAgregarCliente:
	mdlClientes = ModeloClientes()
	def __init__(self, parent):
		self.parent = parent

	def run(self):
		self.frame = FrameAgregarCliente(self.parent)
		self.frame.btn_cancelar.SetFocus()
		self.cargarFecha()
		self.cargarValidadores()
		rpta = self.frame.ShowModal()
		if rpta == wx.ID_OK:
			self.AgregarCliente()

	def cargarValidadores(self):
		self.frame.tc_codigo.SetValidator(ValidarCodigo())

	def cargarFecha(self):
		self.frame.tc_alta.SetValue(time.strftime("%d-%m-%Y"))

	def AgregarCliente(self):
		self.mdlClientes.codigo = self.frame.tc_codigo.GetValue()
		self.mdlClientes.apenom = self.frame.tc_apenom.GetValue().upper()
		self.mdlClientes.domicilio = self.frame.tc_domicilio.GetValue().upper()
		self.mdlClientes.telefonos = self.frame.tc_telefonos.GetValue()
		self.mdlClientes.barrio = self.frame.tc_barrio.GetValue().upper()
		self.mdlClientes.localidad = self.frame.tc_localidad.GetValue().upper()
		self.mdlClientes.seccion = self.frame.tc_seccion.GetValue()
		self.mdlClientes.zona = self.frame.tc_zona.GetValue()
		self.mdlClientes.descripcion = self.frame.tc_descripcion.GetValue()
		self.mdlClientes.create()


	
