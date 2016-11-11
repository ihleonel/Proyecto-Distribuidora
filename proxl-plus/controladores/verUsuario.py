# -*- coding : utf-8 -*-
import wx
from vistas.frame_ver_usuario import FrameVerUsuario
from modelos.modelUsuarios import ModeloUsuarios
from modelos.modelTiposUsuario import ModeloTiposUsuario

class ControladorVerUsuario:
	mdlTUsu = ModeloTiposUsuario()
	mdlUsuarios = ModeloUsuarios()
	def __init__(self, parent, seleccionado):
		self.parent = parent
		self.seleccionado = seleccionado

	def run(self):
		self.frame = FrameVerUsuario(self.parent)
		self.frame.btn_visto.SetFocus()
		self.cargarDatos()
		self.frame.ShowModal()
		
	def cargarDatos(self):
		self.mdlUsuarios.usuario = self.seleccionado
		usu = self.mdlUsuarios.read()
		self.frame.tc_usuario.SetValue(usu['usuario'])
		self.frame.tc_clave.SetValue(usu['clave'])
		self.frame.tc_tipo.SetValue(usu['tipo'])
		self.mdlTUsu.tipo = self.frame.tc_tipo.GetValue()
		datos = self.mdlTUsu.read()
		self.frame.tc_descripcion.SetValue(datos['descripcion'])