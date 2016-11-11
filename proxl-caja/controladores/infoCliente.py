# -*- coding: utf-8 -*-
import wx
from datetime import datetime
from vistas.frame_caja_info_cliente import FrameCajaInfoCliente

from modelos.modelMovimientos import ModeloMovimientos
from modelos.modelMovimientoClientes import ModeloMovimientoClientes
from modelos.modelArticulos import ModeloArticulos

from controladores.modificarCliente import ControladorModificarCliente

from validadores.validarOpCaja import Monto

class ControladorInfoCliente:

	mdlArt = ModeloArticulos()
	mdlMov = ModeloMovimientos()
	mdlMovCli = ModeloMovimientoClientes()

	def __init__(self, parent, infoCaja, infoCli):
		self.parent = parent
		self.infoCaja = infoCaja
		self.infoCli = infoCli

	def run(self):
		self.frame = FrameCajaInfoCliente(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		self.frame.btn_aceptar.SetFocus()
		self.frame.tc_boleta.Enable(False)
		self.frame.tc_oficina.Enable(False)
		self.cargarDatos()
		self.carpturarEventos()
		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.Aceptar()

	def carpturarEventos(self):
		self.frame.btn_editar.Bind(wx.EVT_BUTTON, self.Editar)
		self.frame.rb_efectivo.Bind(wx.EVT_RADIOBUTTON, self.RbEfectivo)
		self.frame.rb_boleta.Bind(wx.EVT_RADIOBUTTON, self.RbBoleta)
		self.frame.tc_boleta.Bind(wx.EVT_TEXT_ENTER, self.EnterTcBoleta)
		self.frame.rb_oficina.Bind(wx.EVT_RADIOBUTTON, self.RbOficina)
		self.frame.tc_oficina.Bind(wx.EVT_TEXT_ENTER, self.EnterTcOficina)

		self.frame.rb_rebotes.Bind(wx.EVT_RADIOBOX, self.RbOtros)
		self.frame.btn_aceptar.Bind(wx.EVT_KEY_DOWN, self.presTecla)

	def cargarDatos(self):
		self.frame.tc_codigo.SetValue(self.infoCli['codigo'])
		self.frame.tc_apenom.SetValue(self.infoCli['nombre'])
		self.frame.tc_zona.SetValue(self.infoCli['zona'])
		self.frame.tc_campania.SetValue(self.infoCli['campania'])
		self.frame.tc_deuda.SetValue(str(self.infoCli['deuda']))
		if self.infoCli['deuda'] == 0:
			#Si el cliente no tiene deuda se deshabilitaran las operaciones de pago, por razones de seguridad.
			self.frame.rb_efectivo.Enable(False)
			self.frame.rb_boleta.Enable(False)
			self.frame.rb_oficina.Enable(False)
			#Y por defecto se marca como efectivo.
			self.frame.rb_efectivo.SetValue(True)

		
		if self.infoCli['entregado'] != None:
			self.frame.cb_entregado.SetValue(True)

		if self.infoCli['forma_pago'] == 1:
			self.frame.rb_efectivo.SetValue(True)
		elif self.infoCli['forma_pago'] == 2:
			self.frame.rb_boleta.SetValue(True)
		elif self.infoCli['forma_pago'] == 3:
			self.frame.rb_oficina.SetValue(True)

		if self.infoCli['forma_pago'] in [1, 2 ,3] and self.infoCli['entregado'] != None:
			self.frame.btn_aceptar.Enable(False)
			self.frame.rb_efectivo.Enable(False)
			self.frame.rb_boleta.Enable(False)
			self.frame.rb_oficina.Enable(False)


		if self.infoCli['forma_pago'] in [1, 2 ,3]:
			self.frame.rb_efectivo.Enable(False)
			self.frame.rb_boleta.Enable(False)
			self.frame.rb_oficina.Enable(False)

		if self.infoCli['rebote'] == "Ninguno":
			self.frame.rb_rebotes.SetSelection(0)
		elif self.infoCli['rebote'] == "A":
			self.frame.rb_rebotes.SetSelection(1)
		elif self.infoCli['rebote'] == "S/B":
			self.frame.rb_rebotes.SetSelection(2)
		elif self.infoCli['rebote'] == "D/E":
			self.frame.rb_rebotes.SetSelection(3)
		elif self.infoCli['rebote'] == "ADC":
			self.frame.rb_rebotes.SetSelection(4)
		else:
			self.frame.rb_rebotes.SetSelection(5)
			self.frame.tc_otros.SetValue(self.infoCli['rebote'])

	def Editar(self, event):
		modifCli = ControladorModificarCliente(self.frame, self.infoCli['codigo'])
		modifCli.run()
		self.cargarDatos()


	def Aceptar(self):
		self.mdlArt.cam_anio = self.infoCli['anio']
		self.mdlArt.cam_num = self.infoCli['num']
		self.mdlArt.lis_numero = self.infoCli['lis']
		self.mdlArt.cli_codigo = self.infoCli['codigo']
		self.mdlArt.deuda = self.infoCli['deuda']
		self.mdlArt.camp = self.infoCli['campania']
		if self.frame.cb_entregado.GetValue():
			self.mdlArt.entregado = datetime.today().strftime("%Y-%m-%d")
			self.mdlArt.medio_entr = 1 #Medio de entrega por caja.
		else:
			self.mdlArt.entregado = '0000-00-00'
			
		if self.infoCli['deuda'] != 0:
			if self.frame.rb_efectivo.GetValue():
				self.mdlArt.forma_pago = 1
			elif self.frame.rb_boleta.GetValue():
				self.mdlArt.forma_pago = 2
			elif self.frame.rb_oficina.GetValue():
				self.mdlArt.forma_pago = 3
		else:
			self.mdlArt.forma_pago = 1

		if self.frame.rb_rebotes.GetSelection() == 0:
			self.mdlArt.rebote = "Ninguno"
		elif self.frame.rb_rebotes.GetSelection() == 1:
			self.mdlArt.rebote = "A"
		elif self.frame.rb_rebotes.GetSelection() == 2:
			self.mdlArt.rebote = "S/B"
		elif self.frame.rb_rebotes.GetSelection() == 3:
			self.mdlArt.rebote = "D/E"
		elif self.frame.rb_rebotes.GetSelection() == 4:
			self.mdlArt.rebote = "ADC"
		else:
			self.mdlArt.rebote = self.frame.tc_otros.GetValue()

		self.mdlArt.update()
		
 		# Guardar en caja.
		self.mdlMovCli.mcam_anio = self.infoCaja['campAnio']
		self.mdlMovCli.mcam_num = self.infoCaja['campNum']
		self.mdlMovCli.mcaj_numero = self.infoCaja['numero']

		self.mdlMovCli.mcli_codigo = self.infoCli['codigo']
		self.mdlMovCli.movcli_monto = self.infoCli['deuda']

		if self.mdlMovCli.existe() == 0:

			if self.frame.cb_entregado.GetValue():
				self.mdlMovCli.movcli_entregado = 1
			else:
				self.mdlMovCli.movcli_entregado = 0

			if self.frame.rb_efectivo.GetValue():
				self.mdlMovCli.movcli_forma_pago = 1
				self.mdlMovCli.movcli_diferencia = 0.0
			elif self.frame.rb_boleta.GetValue():
				self.mdlMovCli.movcli_forma_pago = 2
				self.mdlMovCli.movcli_diferencia = float(self.frame.tc_boleta.GetValue())
			elif self.frame.rb_oficina.GetValue():
				self.mdlMovCli.movcli_forma_pago = 3
				self.mdlMovCli.movcli_diferencia = float(self.frame.tc_oficina.GetValue())
			else:
				self.mdlMovCli.movcli_forma_pago = 0
				self.mdlMovCli.movcli_diferencia = 0.0

			self.mdlMovCli.create()
		else:
			if self.frame.cb_entregado.GetValue():
				self.mdlMovCli.movcli_entregado = 1
			else:
				self.mdlMovCli.movcli_entregado = 0

			self.mdlMovCli.update_e()
			

	def RbEfectivo(self, event):
		self.frame.tc_oficina.Clear()
		self.frame.tc_boleta.Clear()
		self.frame.tc_boleta.Enable(False)
		self.frame.tc_oficina.Enable(False)

	def RbBoleta(self, event):
		self.frame.tc_oficina.Clear()
		self.frame.tc_boleta.Clear()
		self.frame.tc_boleta.Enable(True)
		self.frame.tc_oficina.Enable(False)
		self.frame.tc_boleta.SetFocus()
		self.frame.tc_boleta.SetValue(str(self.infoCli['deuda']))
		self.frame.tc_boleta.SelectAll()

	def EnterTcBoleta(self, event):
		self.frame.tc_oficina.Clear()


	def RbOficina(self, event):
		self.frame.tc_oficina.Clear()
		self.frame.tc_boleta.Clear()
		self.frame.tc_boleta.Enable(False)
		self.frame.tc_oficina.Enable(True)
		self.frame.tc_oficina.SetFocus()
		self.frame.tc_oficina.SetValue(str(self.infoCli['deuda']))
		self.frame.tc_oficina.SelectAll()

	def EnterTcOficina(self, event):
		self.frame.tc_boleta.Clear()

	def RbOtros(self, event):
		if self.frame.rb_rebotes.GetSelection() == 5:
			self.frame.tc_otros.Enable(True)
			self.frame.tc_otros.SetFocus()
		else:
			self.frame.tc_otros.Clear()
			self.frame.tc_otros.Enable(False)


	def presTecla(self, event):
		if event.GetKeyCode() == wx.WXK_NUMPAD1:
			self.frame.rb_efectivo.SetValue(True)
			self.RbEfectivo(None)
		elif event.GetKeyCode() == wx.WXK_NUMPAD2:
			self.frame.cb_entregado.SetValue(True)
			self.frame.rb_boleta.SetValue(True)
			self.RbBoleta(None)
		elif event.GetKeyCode() == wx.WXK_NUMPAD3:
			self.frame.cb_entregado.SetValue(True)
			self.frame.rb_oficina.SetValue(True)
			self.RbOficina(None)
		elif event.GetKeyCode() == wx.WXK_NUMPAD7:
			self.frame.rb_rebotes.SetSelection(0)
		elif event.GetKeyCode() == wx.WXK_NUMPAD8:
			self.frame.rb_rebotes.SetSelection(1)
		elif event.GetKeyCode() == wx.WXK_NUMPAD9:
			self.frame.rb_rebotes.SetSelection(2)
		elif event.GetKeyCode() == wx.WXK_NUMPAD4:
			self.frame.rb_rebotes.SetSelection(3)
		elif event.GetKeyCode() == wx.WXK_NUMPAD5:
			self.frame.rb_rebotes.SetSelection(4)
		elif event.GetKeyCode() == wx.WXK_NUMPAD6:
			self.frame.rb_rebotes.SetSelection(5)
			self.RbOtros(None)
		elif event.GetKeyCode() == wx.WXK_NUMPAD0:
			self.frame.cb_entregado.SetValue(not self.frame.cb_entregado.GetValue())

		event.Skip()