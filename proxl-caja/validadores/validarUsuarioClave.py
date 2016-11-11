# -*- coding:utf-8 -*-
import wx
from modelos.modelUsuarios import ModeloUsuarios
class Usuario_s(wx.PyValidator):
	mdlUsuarios = ModeloUsuarios()
	def __init__(self):
		wx.PyValidator.__init__(self)
		
	def Clone(self):
		return Usuario_s()
		
	def Validate(self, win):
		tctrl = self.GetWindow()
		texto = tctrl.GetValue()
		self.mdlUsuarios.usuario = texto
		if len(texto) == 0:
			tctrl.SetBackgroundColour("pink")
			tctrl.SetFocus()
			tctrl.Refresh()
			return False
		elif self.mdlUsuarios.existUser() != 1:
			tctrl.SetBackgroundColour("pink")
			tctrl.SetFocus()
			tctrl.Refresh()
			return False
		else:
			tctrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
			tctrl.Refresh()
			return True

	def TransferToWindow(self):
		return True
		
	def TransferFromWindow(self):
		return True

class Clave_s(wx.PyValidator):
	mdlUsuarios = ModeloUsuarios()
	def __init__(self):
		wx.PyValidator.__init__(self)

	def Clone(self):
		return Clave_s()

	def Validate(self, win):
		tctrl = self.GetWindow()
		texto = tctrl.GetValue()
		self.mdlUsuarios.usuario = win.tc_usuario.GetValue()
		self.mdlUsuarios.clave = texto
		if len(texto) == 0:
			tctrl.SetBackgroundColour("pink")
			tctrl.SetFocus()
			tctrl.Refresh()
			return False
		elif self.mdlUsuarios.existUserKey() != 1:
			tctrl.SetBackgroundColour("pink")
			tctrl.SetFocus()
			tctrl.Refresh()
			return False
		elif self.mdlUsuarios.typeUser() != 'Administrador':
			wx.MessageBox(u"El usuario ingresado no posee los permisos para acceder a esta aplicación", "Tipo de usuario inadecuado")
			tctrl.Refresh()
			return False
		else:
			tctrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
			tctrl.Refresh()
			return True

	def TransferToWindow(self):
		return True
		
	def TransferFromWindow(self):
		return True