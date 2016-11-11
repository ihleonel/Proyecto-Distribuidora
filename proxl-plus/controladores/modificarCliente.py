# -*- coding: utf-8 -*-
import wx
import time
from modelos.modelClientes import ModeloClientes
from validadores.validarCliente import ValidarCodigo
from vistas.frame_modificar_cliente import FrameModificarCliente

class ControladorModificarCliente:
	mdlClientes = ModeloClientes()

	def __init__(self, parent, seleccionado):
		self.parent = parent
		self.Seleccionado = seleccionado
		self.Telefono = None

	def run(self):
		self.frame = FrameModificarCliente(self.parent)
		self.frame.btn_cancelar.SetFocus()
		self.cargarDatos()
		self.capturarEventos()
		rpta = self.frame.ShowModal()
		if rpta == wx.ID_OK:
			self.ModificarCliente()

	def capturarEventos(self):
		self.frame.tc_apenom.Bind(wx.EVT_LEFT_UP, self.seleccionarApenom)
		self.frame.tc_domicilio.Bind(wx.EVT_LEFT_UP, self.seleccionarDomicilio)
		self.frame.tc_telefonos.Bind(wx.EVT_LEFT_UP, self.seleccionarTelefono)
		self.frame.tc_barrio.Bind(wx.EVT_LEFT_UP, self.seleccionarBarrio)
		self.frame.tc_localidad.Bind(wx.EVT_LEFT_UP, self.seleccionarLocalidad)
		self.frame.tc_seccion.Bind(wx.EVT_LEFT_UP, self.seleccionarSeccion)

	def cargarDatos(self):
		self.mdlClientes.codigo = self.Seleccionado
		self.datos = self.mdlClientes.read_with_ruta()

		self.frame.tc_codigo.SetValue(self.datos['codigo'])
		self.frame.tc_apenom.SetValue(self.datos['nombre'])
		self.frame.tc_zona.SetValue(self.datos['zona'])
		self.frame.tc_domicilio.SetValue(self.datos['domicilio'])
		self.frame.tc_telefonos.SetValue(self.datos['telefonos'])
		self.frame.tc_barrio.SetValue(self.datos['barrio'])
		self.frame.tc_localidad.SetValue(self.datos['localidad'])
		self.frame.tc_seccion.SetValue(self.datos['seccion'])
		self.frame.tc_descripcion.SetValue(str(self.datos['descripcion']))
		self.frame.tc_alta.SetValue(str(self.datos['alta']))
		self.frame.c_referencia.SetSelection(self.datos['referencia'])


	def ModificarCliente(self):
		self.mdlClientes.codigo = self.frame.tc_codigo.GetValue()
		self.mdlClientes.apenom = self.frame.tc_apenom.GetValue().upper()
		self.mdlClientes.domicilio = self.frame.tc_domicilio.GetValue().upper()
		self.mdlClientes.telefonos = self.frame.tc_telefonos.GetValue()
		self.mdlClientes.barrio = self.frame.tc_barrio.GetValue().upper()
		self.mdlClientes.localidad = self.frame.tc_localidad.GetValue().upper()
		self.mdlClientes.seccion = self.frame.tc_seccion.GetValue()
		self.mdlClientes.zona = self.frame.tc_zona.GetValue()
		self.mdlClientes.descripcion = self.frame.tc_descripcion.GetValue()
		self.mdlClientes.crut_id = self.datos['ruta_id']
		self.mdlClientes.orden = self.datos['orden'] 
		self.mdlClientes.referencia = self.frame.c_referencia.GetSelection()
		self.mdlClientes.update()

	def seleccionarApenom(self, event):
		self.frame.tc_apenom.SetSelection(-1, -1)
		event.Skip()

	def seleccionarDomicilio(self, event):
		self.frame.tc_domicilio.SelectAll()
		event.Skip()

	def seleccionarTelefono(self, event):
		self.frame.tc_telefonos.SelectAll()
		event.Skip()

	def seleccionarBarrio(self, event):
		self.frame.tc_barrio.SelectAll()
		event.Skip()

	def seleccionarLocalidad(self, event):
		self.frame.tc_localidad.SelectAll()
		event.Skip()

	def seleccionarSeccion(self, event):
		self.frame.tc_seccion.SelectAll()
		event.Skip()


