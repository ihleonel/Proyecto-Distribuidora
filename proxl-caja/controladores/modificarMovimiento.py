# -*- coding: utf-8 -*-
import wx
from datetime import datetime

from vistas.frame_modificar_movimiento import FrameModificarMovimiento

from modelos.modelMovimientoClientes import ModeloMovimientoClientes

from validadores.validarOpCaja import Monto

class ControladorModificarMovimiento:

	mdlMovCli = ModeloMovimientoClientes()

	def __init__(self, parent, selec):
		self.parent = parent
		self.selec = selec

	def run(self):
		self.frame = FrameModificarMovimiento(self.parent)

		loc = wx.IconLocation(r'icono.ico')
		self.frame.SetIcon(wx.IconFromLocation(loc))
		
		self.frame.btn_cancelar.SetFocus()
		self.cargarDatos()
		self.capturarEventos()
		self.cargarValidadores()
		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.Aceptar()

	def cargarDatos(self):
		self.mdlMovCli.mcam_anio = self.selec['anio']
		self.mdlMovCli.mcam_num = self.selec['num']
		self.mdlMovCli.mcaj_numero = self.selec['cnum']
		self.mdlMovCli.mcli_codigo = self.selec['codigo']
		self.datos = self.mdlMovCli.read()

		self.frame.tc_codigo.SetValue(self.datos[0])
		self.frame.tc_apenom.SetValue(self.datos[1])
		self.frame.tc_deuda.SetValue(str(self.datos[2]))

		val = self.datos[3] != '0000-00-00'
		self.frame.cb_entregado.SetValue(val)

		if self.datos[4] == 1:
			self.frame.rb_efectivo.SetValue(True)
			self.frame.tc_dif_recibo.Enable(False)
			self.frame.tc_dif_recibo.Clear()
			self.frame.tc_dif_boleta.Enable(False)
			self.frame.tc_dif_boleta.Clear()
		elif self.datos[4] == 2:
			self.frame.rb_boleta.SetValue(True)
			self.frame.tc_dif_boleta.Enable(True)
			self.frame.tc_dif_boleta.SetValue(str(self.datos[5]))
			self.frame.tc_dif_recibo.Clear()
			self.frame.tc_dif_recibo.Enable(False)
		elif self.datos[4] == 3:
			self.frame.rb_recibo.SetValue(True)
			self.frame.tc_dif_recibo.Enable(True)
			self.frame.tc_dif_recibo.SetValue(str(self.datos[5]))
			self.frame.tc_dif_boleta.Clear()
			self.frame.tc_dif_boleta.Enable(False)


	def capturarEventos(self):
		self.frame.rb_efectivo.Bind(wx.EVT_RADIOBUTTON, self.RbEfectivo)
		self.frame.rb_boleta.Bind(wx.EVT_RADIOBUTTON, self.RbBoleta)
		self.frame.rb_recibo.Bind(wx.EVT_RADIOBUTTON, self.RbRecibo)

	def cargarValidadores(self):
		self.frame.tc_deuda.SetValidator(Monto())

	def RbEfectivo(self, event):
		self.frame.tc_dif_recibo.Enable(False)
		self.frame.tc_dif_recibo.Clear()
		self.frame.tc_dif_boleta.Enable(False)
		self.frame.tc_dif_boleta.Clear()

	def RbBoleta(self, event):
		self.frame.tc_dif_boleta.Enable(True)
		if self.datos[5] != 0:
			self.frame.tc_dif_boleta.SetValue(str(self.datos[5]))
		else:
			self.frame.tc_dif_boleta.SetValue(str(self.datos[2]))

		self.frame.tc_dif_recibo.Clear()
		self.frame.tc_dif_recibo.Enable(False)

	def RbRecibo(self, event):
		self.frame.tc_dif_recibo.Enable(True)
		if self.datos[5] != 0:
			self.frame.tc_dif_recibo.SetValue(str(self.datos[5]))
		else:
			self.frame.tc_dif_recibo.SetValue(str(self.datos[2]))
			
		self.frame.tc_dif_boleta.Clear()
		self.frame.tc_dif_boleta.Enable(False)

	def Aceptar(self):
		self.mdlMovCli.movcli_monto = float(self.frame.tc_deuda.GetValue())
		
		if self.frame.cb_entregado.GetValue():
			self.mdlMovCli.movcli_entregado = 1
		else:
			self.mdlMovCli.movcli_entregado = 0

		if self.frame.rb_efectivo.GetValue():
			self.mdlMovCli.movcli_forma_pago = 1
			self.mdlMovCli.movcli_diferencia = 0.0
		elif self.frame.rb_boleta.GetValue():
			self.mdlMovCli.movcli_forma_pago = 2
			self.mdlMovCli.movcli_diferencia = float(self.frame.tc_dif_boleta.GetValue())
		elif self.frame.rb_recibo.GetValue():
			self.mdlMovCli.movcli_forma_pago = 3
			self.mdlMovCli.movcli_diferencia = float(self.frame.tc_dif_recibo.GetValue())
		else:
			self.mdlMovCli.movcli_forma_pago = 0
			self.mdlMovCli.movcli_diferencia = 0.0

		self.mdlMovCli.update()

