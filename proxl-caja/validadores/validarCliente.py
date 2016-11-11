# -*- coding:utf-8 -*-
import wx
from modelos.modelClientes import ModeloClientes
class ValidarCodigo(wx.PyValidator):
	mdlClientes = ModeloClientes()

	def __init__(self):
		wx.PyValidator.__init__(self)
		
	def Clone(self):
		return ValidarCodigo()
		
	def Validate(self, win):
		tctrl = self.GetWindow()
		texto = tctrl.GetValue()
		self.mdlClientes.codigo = texto
		if len(texto) == 0:
			wx.MessageBox(u"Este campo NO puede omitirse!", u"Se esta olvidando de algo!")
			tctrl.SetBackgroundColour("pink")
			tctrl.SetFocus()
			tctrl.Refresh()
			return False
		elif self.mdlClientes.exist():
			wx.MessageBox(u"EL código de cliente ya existe", u"Revisar")
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
		