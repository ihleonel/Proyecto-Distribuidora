# -*- coding : utf-8 -*-
import wx
from vistas.frame_agregar_usuario import FrameAgregarUsuario
from modelos.modelUsuarios import ModeloUsuarios
from modelos.modelTiposUsuario import ModeloTiposUsuario
from validadores.validarNuevoUsuario import NuevoUsuario, NuevoUsuarioClave, NuevoUsuarioTipo

class ControladorAgregarUsuario:
	mdlTUsu = ModeloTiposUsuario()
	mdlUsuarios = ModeloUsuarios()
	def __init__(self, parent):
		self.parent = parent

	def run(self):
		self.frame = FrameAgregarUsuario(self.parent)
		self.capturarEventos()
		self.cargarValidadores()
		resp = self.frame.ShowModal()
		if resp == wx.ID_OK:
			self.Agregar()

	def capturarEventos(self):
		self.frame.ch_tipo.Bind(wx.EVT_CHOICE, self.cargarDescripcion)

	def cargarValidadores(self):
		self.frame.tc_usuario.SetValidator(NuevoUsuario())
		self.frame.tc_clave.SetValidator(NuevoUsuarioClave())
		self.frame.ch_tipo.SetValidator(NuevoUsuarioTipo())

	''' Evento de choice. '''
	def cargarDescripcion(self, event):
		if self.frame.ch_tipo.GetStringSelection() != '--Seleccionar--':
			self.mdlTUsu.tipo = self.frame.ch_tipo.GetStringSelection()
			datos = self.mdlTUsu.read()
			self.frame.tc_descripcion.SetValue(datos['descripcion'])
		else:
			self.frame.tc_descripcion.SetValue("")

	def Agregar(self):
		self.mdlUsuarios.usuario = self.frame.tc_usuario.GetValue()
		self.mdlUsuarios.clave = self.frame.tc_clave.GetValue()
		self.mdlUsuarios.tipo = self.frame.ch_tipo.GetStringSelection()
		self.mdlUsuarios.create()