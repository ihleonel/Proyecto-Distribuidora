# -*- coding: utf-8 -*-
import wx
from modelos.modelClientes import ModeloClientes
from vistas.frame_ver_cliente import FrameVerCliente

class ControladorDetalleCliente:
	mdlClientes = ModeloClientes()

	def __init__(self, parent, seleccionado):
		self.parent = parent
		self.Seleccionado = seleccionado

	def run(self):
		self.frame = FrameVerCliente(self.parent)
		self.frame.btn_visto.SetFocus()
		self.cargarDatos()
		self.frame.ShowModal()
	
	def cargarDatos(self):
		self.mdlClientes.codigo = self.Seleccionado
		datos = self.mdlClientes.read()

		self.frame.tc_codigo.SetValue(datos['codigo'])
		self.frame.tc_apenom.SetValue(datos['nombre'])
		self.frame.tc_zona.SetValue(datos['zona'])
		self.frame.tc_domicilio.SetValue(datos['domicilio'])
		self.frame.tc_telefonos.SetValue(datos['telefonos'])
		self.frame.tc_barrio.SetValue(datos['barrio'])
		self.frame.tc_localidad.SetValue(datos['localidad'])
		self.frame.tc_seccion.SetValue(datos['seccion'])
		self.frame.tc_descripcion.SetValue(str(datos['descripcion']))
		self.frame.tc_alta.SetValue(str(datos['alta']))