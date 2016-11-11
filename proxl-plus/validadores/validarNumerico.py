# -*- coding:utf-8 -*-
import wx
class ValidarFlotante(wx.PyValidator):
	def __init__(self):
		wx.PyValidator.__init__(self)
		
	def Clone(self):
		return ValidarFlotante()
		
	def Validate(self, win):
		tctrl = self.GetWindow()
		texto = tctrl.GetValue()
		if len(texto) == 0:
			tctrl.SetBackgroundColour("pink")
			tctrl.SetFocus()
			tctrl.Refresh()
			return False
		elif not self.isfloat(texto):
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

	def isfloat(self, f):
		try:
			float(f)
			return True
		except:
			return False

class ValidarEntero(wx.PyValidator):
	def __init__(self):
		wx.PyValidator.__init__(self)
		
	def Clone(self):
		return ValidarEntero()
		
	def Validate(self, win):
		tctrl = self.GetWindow()
		texto = tctrl.GetValue()
		if len(texto) == 0:
			tctrl.SetBackgroundColour("pink")
			tctrl.SetFocus()
			tctrl.Refresh()
			return False
		elif not self.isint(texto):
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

	def isint(self, f):
		try:
			int(f)
			return True
		except:
			return False
		