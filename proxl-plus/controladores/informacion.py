# -*- coding : utf-8 -*-
import wx
from datetime import datetime
from vistas.frame_informacion import FrameInformacion

from modelos.modelArticulos import ModeloArticulos
from validadores.validarNumerico import ValidarFlotante
from controladores.modificarCliente import ControladorModificarCliente

class ControladorInformacion:
	mdlArt = ModeloArticulos()
	def __init__(self, parent, camp, cod):
		self.parent = parent
		self.aCamp = camp
		self.cod = cod

	def run(self):
		self.frame = FrameInformacion(self.parent)
		self.frame.btn_aceptar.SetFocus()
		self.capturarEventos()
		self.cargarValidadores()
		self.cargarDatos()
		resp = self.frame.ShowModal()
		if resp == wx.ID_OK:
			self.Aceptar()

	def capturarEventos(self):
		self.frame.btn_editar.Bind(wx.EVT_BUTTON, self.Editar)
		self.frame.btn_aceptar.Bind(wx.EVT_KEY_DOWN, self.presTecla)
		self.frame.rb_rebotes.Bind(wx.EVT_RADIOBOX, self.RbOtros)
		self.frame.rb_efectivo.Bind(wx.EVT_LEFT_DCLICK, self.DesmarcarEfectivo)
		self.frame.rb_boleta.Bind(wx.EVT_LEFT_DCLICK, self.DesmarcarBoleta)
		self.frame.rb_oficina.Bind(wx.EVT_LEFT_DCLICK, self.DesmarcarOficina)

	def cargarValidadores(self):
		self.frame.tc_deuda.SetValidator(ValidarFlotante())

	def cargarDatos(self):
		self.mdlArt.cam_anio = self.aCamp['anio'] #PK
		self.mdlArt.cam_num = self.aCamp['numero']#PK
		self.mdlArt.cli_codigo = self.cod 		  #PK
		self.info = self.mdlArt.read()
		self.mdlArt.lis_numero = self.info['lis']      #PK
		self.frame.tc_codigo.SetValue(self.info['codigo'])
		self.frame.tc_apenom.SetValue(self.info['nombre'])
		self.frame.tc_zona.SetValue(self.info['zona'])
		self.frame.tc_campania.SetValue(self.info['campania'])
		self.frame.tc_deuda.SetValue(str(self.info['deuda']))
		if str(self.info['entregado']) != "None" :
			self.frame.cb_entregado.SetValue(True)
			self.frame.tc_entregado.SetValue(self.date_format(self.info['entregado']))
		if self.info['forma_pago'] == 1:
			self.frame.rb_efectivo.SetValue(True)
		elif self.info['forma_pago'] == 2:
			self.frame.rb_boleta.SetValue(True)
		elif self.info['forma_pago'] == 3:
			self.frame.rb_oficina.SetValue(True)

		if self.info['rebote'] == "Ninguno":
			self.frame.rb_rebotes.SetSelection(0)
		elif self.info['rebote'] == "A":
			self.frame.rb_rebotes.SetSelection(1)
		elif self.info['rebote'] == "S/B":
			self.frame.rb_rebotes.SetSelection(2)
		elif self.info['rebote'] == "R/D":
			self.frame.rb_rebotes.SetSelection(3)
		elif self.info['rebote'] == "ADC":
			self.frame.rb_rebotes.SetSelection(4)
		else:
			self.frame.rb_rebotes.SetSelection(5)
			self.frame.tc_otros.SetValue(self.info['rebote'])


	def Aceptar(self):
		self.mdlArt.camp = self.frame.tc_campania.GetValue()
		self.mdlArt.deuda = float(self.frame.tc_deuda.GetValue())

		if self.frame.cb_entregado.GetValue():
			if str(self.info['entregado']) == "None":
				self.mdlArt.entregado = datetime.today().strftime("%Y/%m/%d")
			else:
				self.mdlArt.entregado = self.info['entregado']
		else:
			self.mdlArt.entregado = "0000/00/00"

		if self.frame.rb_efectivo.GetValue():
			self.mdlArt.forma_pago = 1
		elif self.frame.rb_boleta.GetValue():
			self.mdlArt.forma_pago = 2
		elif self.frame.rb_oficina.GetValue():
			self.mdlArt.forma_pago = 3
		else:
			self.mdlArt.forma_pago = 0

		if self.frame.rb_rebotes.GetSelection() == 0:
			self.mdlArt.rebote = "Ninguno"
		elif self.frame.rb_rebotes.GetSelection() == 1:
			self.mdlArt.rebote = "A"
		elif self.frame.rb_rebotes.GetSelection() == 2:
			self.mdlArt.rebote = "S/B"
		elif self.frame.rb_rebotes.GetSelection() == 3:
			self.mdlArt.rebote = "R/D"
		elif self.frame.rb_rebotes.GetSelection() == 4:
			self.mdlArt.rebote = "ADC"
		else:
			self.mdlArt.rebote = self.frame.tc_otros.GetValue()

		self.mdlArt.update()

	def Editar(self, event):
		modifCli = ControladorModificarCliente(self.frame, self.cod)
		modifCli.run()
		self.cargarDatos()

	def presTecla(self, event):
		if event.GetKeyCode() == wx.WXK_NUMPAD1:
			self.frame.cb_entregado.SetValue(True)
			self.frame.rb_efectivo.SetValue(True)
		elif event.GetKeyCode() == wx.WXK_NUMPAD2:
			self.frame.cb_entregado.SetValue(True)
			self.frame.rb_boleta.SetValue(True)
		elif event.GetKeyCode() == wx.WXK_NUMPAD3:
			self.frame.cb_entregado.SetValue(True)
			self.frame.rb_oficina.SetValue(True)
		event.Skip()

	def RbOtros(self, event):
		if self.frame.rb_rebotes.GetSelection() == 6:
			self.frame.tc_otros.Enable(True)
			self.frame.tc_otros.SetFocus()
		else:
			self.frame.tc_otros.Clear()
			self.frame.tc_otros.Enable(False)
		event.Skip()

	def DesmarcarEfectivo(self, event):
		self.frame.rb_efectivo.SetValue(False)
		
	def DesmarcarBoleta(self, event):
		self.frame.rb_boleta.SetValue(False)

	def DesmarcarOficina(self, event):
		self.frame.rb_oficina.SetValue(False)

	def date_format(self, s):
		'Formatea una fecha dada (aaaa-mm-dd  >>  dd-mm-aaaa)'
		s = str(s)
		l = s.split("-")
		l[0], l[2] = l[2], l[0]
		return "-".join(l)