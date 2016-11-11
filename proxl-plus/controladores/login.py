# -*- coding : utf-8 -*-
import wx
from vistas.frame_login import FrameLogin
from modelos.modelUsuarios import ModeloUsuarios
from controladores.principal import ControladorPrincipal

class ControladorLogin:
	mdlUsuarios = ModeloUsuarios()
	def __init__(self):
		pass

	def run(self):
		self.frame = FrameLogin(None)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		self.capturarEventos()
		self.frame.ShowModal()

	def capturarEventos(self):
		self.frame.btn_aceptar.Bind(wx.EVT_BUTTON, self.Validaciones)
		self.frame.tc_usuario.Bind(wx.EVT_TEXT_ENTER, self.ValidarUsuario)
		self.frame.tc_clave.Bind(wx.EVT_TEXT_ENTER, self.ValidarClave)

	def ValidarUsuario(self, event):
		if self.frame.tc_usuario.GetValue() != "":
			self.mdlUsuarios.usuario = self.frame.tc_usuario.GetValue()
			if self.mdlUsuarios.existUser() == 1:
				self.frame.tc_usuario.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
				self.frame.tc_usuario.Refresh()
				self.frame.tc_clave.SetFocus()
			else:
				self.frame.tc_usuario.SetBackgroundColour("pink")
				self.frame.tc_usuario.SetFocus()
				self.frame.tc_usuario.Refresh()
		else:
			self.frame.tc_usuario.SetBackgroundColour("pink")
			self.frame.tc_usuario.SetFocus()
			self.frame.tc_usuario.Refresh()

		event.Skip()

	def ValidarClave(self, event=None):
		if self.frame.tc_usuario.GetValue() != "":
			self.mdlUsuarios.usuario = self.frame.tc_usuario.GetValue()
			
			if self.mdlUsuarios.existUser() == 1:

				if self.frame.tc_clave.GetValue() != "":
					self.mdlUsuarios.clave = self.frame.tc_clave.GetValue()
					if self.mdlUsuarios.existUserKey() == 1:
						self.Continuar()
					else:
						self.frame.tc_clave.SetBackgroundColour("pink")
						self.frame.tc_clave.Refresh()
						self.frame.tc_usuario.SetBackgroundColour("pink")
						self.frame.tc_usuario.SetFocus()
						self.frame.tc_usuario.Refresh()
				else:
					self.frame.tc_clave.SetBackgroundColour("pink")
					self.frame.tc_usuario.SetFocus()
					self.frame.tc_clave.Refresh()
			else:
				self.frame.tc_usuario.SetBackgroundColour("pink")
				self.frame.tc_usuario.SetFocus()
				self.frame.tc_usuario.Refresh()		
		else:
			self.frame.tc_usuario.SetBackgroundColour("pink")
			self.frame.tc_usuario.SetFocus()
			self.frame.tc_usuario.Refresh()
		if event != None:
			event.Skip()

	def Validaciones(self, event):
		self.ValidarClave()

	def Continuar(self):
		principal = ControladorPrincipal(usuario = self.frame.tc_usuario.GetValue())
		principal.run()
		self.frame.Destroy()
