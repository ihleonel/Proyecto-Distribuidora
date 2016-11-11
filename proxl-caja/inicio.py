# -*- coding : utf-8 -*-
"""
	Nombre: inicio.py
	Autor: Ibarra Hector Leonel
	e-mail: ibarra.h.leonel@gmail.com
"""
import wx
from controladores.principal import ControladorPrincipal

if __name__ == '__main__':
	Aplicacion = wx.App()
	wx.Locale(wx.LANGUAGE_SPANISH)
	inicio = ControladorPrincipal()
	inicio.run()
	Aplicacion.MainLoop()
