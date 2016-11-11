# -*- coding : utf-8 -*-
import wx
from vistas.frame_modificar_usuario import FrameModificarUsuario
from modelos.modelUsuarios import ModeloUsuarios
from modelos.modelTiposUsuario import ModeloTiposUsuario
from validadores.validarNuevoUsuario import NuevoUsuarioClave, NuevoUsuarioTipo

class ControladorModificarUsuario:
	mdlTUsu = ModeloTiposUsuario()
	mdlUsuarios = ModeloUsuarios()
	def __init__(self, parent, seleccionado):
		self.parent = parent
		self.seleccionado = seleccionado

	def run(self):
		self.frame = FrameModificarUsuario(self.parent)
		self.frame.btn_cancelar.SetFocus()
		self.capturarEventos()
		self.cargarValidadores()
		self.cargarDatos()
		self.cargarDescripcion()
		resp = self.frame.ShowModal()
		if resp == wx.ID_OK:
			self.Modificar()

	def capturarEventos(self):
		self.frame.ch_tipo.Bind(wx.EVT_CHOICE, self.cargarDescripcion)

	def cargarValidadores(self):
		self.frame.tc_clave.SetValidator(NuevoUsuarioClave())
		self.frame.ch_tipo.SetValidator(NuevoUsuarioTipo())

	def cargarDatos(self):
		self.mdlUsuarios.usuario = self.seleccionado
		usu = self.mdlUsuarios.read()
		self.frame.tc_usuario.SetValue(usu['usuario'])
		self.frame.tc_clave.SetValue(usu['clave'])
		self.frame.ch_tipo.SetStringSelection(usu['tipo'])

	''' Evento de choice. '''
	def cargarDescripcion(self, event = None):
		if self.frame.ch_tipo.GetStringSelection() != '--Seleccionar--':
			self.mdlTUsu.tipo = self.frame.ch_tipo.GetStringSelection()
			datos = self.mdlTUsu.read()
			self.frame.tc_descripcion.SetValue(datos['descripcion'])
		else:
			self.frame.tc_descripcion.SetValue("")

	def Modificar(self):
		self.mdlUsuarios.usuario = self.frame.tc_usuario.GetValue()
		self.mdlUsuarios.clave = self.frame.tc_clave.GetValue()
		self.mdlUsuarios.tipo = self.frame.ch_tipo.GetStringSelection()
		self.mdlUsuarios.update()

		