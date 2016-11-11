# -*- coding utf-8 -*-
import wx
from vistas.frame_historial_clientes import FrameHistorialClientes

from modelos.modelArticulos import ModeloArticulos
from modelos.modelCampanias import ModeloCampanias
from modelos.modelClientes import ModeloClientes

from validadores.validarNumerico import ValidarEntero

class ControladorHistorial:
	mdlArt = ModeloArticulos()
	mdlCamp = ModeloCampanias()
	mdlCli = ModeloClientes()
	def __init__(self, parent):
		self.parent = parent

	def run(self):
		self.frame = FrameHistorialClientes(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		self.capturarEventos()
		self.cargarValidadores()
		self.frame.Show()

	def capturarEventos(self):
		self.frame.btn_buscar.Bind(wx.EVT_BUTTON, self.Buscar)
		self.frame.tc_codigo.Bind(wx.EVT_TEXT_ENTER, self.Buscar)
		self.frame.tc_codigo.Bind(wx.EVT_TEXT, self.AutoCompletar)
		self.frame.btn_salir.Bind(wx.EVT_BUTTON, self.Salir)

	def cargarValidadores(self):
		self.frame.tc_rango.SetValidator(ValidarEntero())

	def Buscar(self, event):
		self.limpiar_grilla()
		self.mdlCli.codigo = self.frame.tc_codigo.GetValue()
		if  self.mdlCli.exist():
			self.frame.tc_codigo.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
			self.frame.tc_codigo.SetFocus()
			self.frame.tc_codigo.Refresh()

			datosCli = self.mdlCli.read()
			rng = int(self.frame.tc_rango.GetValue())
			camps = self.mdlCamp.campaign_in_range(rng)
			hist = self.mdlArt.historialCliente(camps, datosCli['codigo'])

			self.frame.grilla.AppendRows(1)
			self.frame.grilla.SetCellValue(0, 0, datosCli['codigo'])
			self.frame.grilla.SetCellValue(0, 1, datosCli['nombre'])
			self.frame.grilla.SetCellValue(0, 2, datosCli['seccion'])
			self.frame.grilla.SetCellValue(0, 3, datosCli['domicilio'])
			self.frame.grilla.SetCellValue(0, 4, datosCli['barrio'])
			
			col = 5
			for camp in camps:
				etiq = str(camp[1]) +"-"+str(camp[0])
				self.frame.grilla.SetColLabelValue(col, etiq)
				col += 1
			col = 5
			for h in hist:
				self.frame.grilla.SetCellValue(0, col, h)
				col += 1
		else:
			self.frame.tc_codigo.SetBackgroundColour("pink")
			self.frame.tc_codigo.SetFocus()
			self.frame.tc_codigo.Refresh()

	def AutoCompletar(self, event):
		prefijo = self.frame.tc_codigo.GetValue()
		if len(prefijo) == 4:
			sufijo = prefijo[-1]
			if sufijo != "/": 
				prefijo = prefijo[:3] + "/"
				prefijo += sufijo
				self.frame.tc_codigo.SetValue(prefijo)
		self.frame.tc_codigo.SetInsertionPoint(len(prefijo))
		event.Skip()

	def limpiar_grilla(self):
		for i in range(self.frame.grilla.GetNumberRows()):
			self.frame.grilla.DeleteRows(0, 1)

	def Salir(self, event):
		self.frame.Destroy()