# -*- coding:utf-8 -*-
import wx
from modelos.modelUsuarios import ModeloUsuarios
class NuevoUsuario(wx.PyValidator):
	mdlUsuarios = ModeloUsuarios()
	def __init__(self):
		wx.PyValidator.__init__(self)
		
	def Clone(self):
		return NuevoUsuario()
		
	def Validate(self, win):
		tctrl = self.GetWindow()
		texto = tctrl.GetValue()
		self.mdlUsuarios.usuario = texto
		if len(texto) == 0:
			tctrl.SetBackgroundColour("pink")
			tctrl.SetFocus()
			tctrl.Refresh()
			return False
		elif self.mdlUsuarios.existUser() == 1:
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

class NuevoUsuarioClave(wx.PyValidator):
	def __init__(self):
		wx.PyValidator.__init__(self)
		
	def Clone(self):
		return NuevoUsuarioClave()
		
	def Validate(self, win):
		tctrl = self.GetWindow()
		texto = tctrl.GetValue()
		if len(texto) == 0:
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

class NuevoUsuarioTipo(wx.PyValidator):
	def __init__(self):
		wx.PyValidator.__init__(self)
		
	def Clone(self):
		return NuevoUsuarioTipo()
		
	def Validate(self, win):
		tctrl = self.GetWindow()
		texto = tctrl.GetStringSelection()
		if texto == "--Seleccionar--":
			wx.MessageBox("Debe seleccionar un tipo de usuario.", "Se esta olvidando de algo!")
			tctrl.SetFocus()
			return False
		else:
			return True

	def TransferToWindow(self):
		return True
		
	def TransferFromWindow(self):
		return True

