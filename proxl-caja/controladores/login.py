# -*- coding : utf-8 -*-
import wx
from vistas.frame_login import FrameLogin
from validadores.validarUsuarioClaveCaja import Usuario, Clave
from validadores.validarUsuarioClave import Usuario_s, Clave_s

class ControladorLogin:
	def __init__(self, parent, modo):
		self.parent = parent
		self.modo = modo #Determina los permisos para el acceso.

	def run(self):
		self.frame = FrameLogin(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		self.cargarValidadores()
		resp = self.frame.ShowModal()
		if resp == wx.ID_OK:
			usu = {'nom': self.frame.tc_usuario.GetValue(), 
					'cla': self.frame.tc_clave.GetValue()}
			return usu
		else:
			return {}

	def cargarValidadores(self):
		if self.modo:	
			self.frame.tc_usuario.SetValidator(Usuario_s())
			self.frame.tc_clave.SetValidator(Clave_s())
		else:
			self.frame.tc_usuario.SetValidator(Usuario())
			self.frame.tc_clave.SetValidator(Clave())
