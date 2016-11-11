# -*- coding:utf-8 -*-
import wx
class Validar(wx.PyValidator):
	def __init__(self):
		wx.PyValidator.__init__(self)
		
	def Clone(self):
		return Validar()
		
	def Validate(self, win):
		tctrl = self.GetWindow()
		texto = tctrl.GetValue()
		if len(texto) == 0:
			wx.MessageBox("Este campo NO puede omitirse!", "Se esta olvidando de algo!")
			tctrl.SetBackgroundColour("pink")
			tctrl.SetFocus()
			tctrl.Refresh()
			return False
		elif not texto.isdigit():
			wx.MessageBox("Este campo solo adminte caracteres numericos mayores que cero.", "EL valor ingresado no es valido!")
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
		