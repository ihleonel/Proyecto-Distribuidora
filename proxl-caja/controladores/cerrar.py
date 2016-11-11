# -*- coding: utf-8 -*-
import wx
from datetime import datetime
from vistas.frame_caja_cerrar import FrameCerrarCaja
from validadores.validarNoVacio import NoVacio

from modelos.modelCajas import ModeloCajas
from modelos.modelMovimientos import ModeloMovimientos
from modelos.modelMovimientoClientes import ModeloMovimientoClientes
from modelos.modelReportes import ModeloReportes

class ControladorCerrarCaja:
	mdlCaj = ModeloCajas()
	mdlMov = ModeloMovimientos()
	mdlMovCli = ModeloMovimientoClientes()

	def __init__(self, parent, infoCaja):
		self.parent = parent
		self.infoCaja = infoCaja

	def run(self):
		self.frame = FrameCerrarCaja(self.parent)
		self.capturarEventos()
		self.cargarDatos()
		self.cargarValidadores()
		rta = self.frame.ShowModal()
		if rta == wx.ID_OK:
			self.Aceptar()

	def capturarEventos(self):
		self.frame.btn_buscar.Bind(wx.EVT_BUTTON, self.Buscar)

	def cargarValidadores(self):
		self.frame.tc_dir.SetValidator(NoVacio())

	def cargarDatos(self):
		self.mdlMov.mcam_anio = self.infoCaja['campAnio']
		self.mdlMov.mcam_num = self.infoCaja['campNum']
		self.mdlMov.mcaj_numero = self.infoCaja['numero']

		self.mdlMovCli.mcam_anio = self.infoCaja['campAnio']
		self.mdlMovCli.mcam_num = self.infoCaja['campNum']
		self.mdlMovCli.mcaj_numero = self.infoCaja['numero']

		ingr = self.mdlMov.totalIngresos() + self.mdlMovCli.totalIngresosClientes()
		egre = self.mdlMov.totalEgresos()
		ttal = ingr - egre

		self.frame.tc_ingresos.SetValue(str(ingr))
		self.frame.tc_egresos.SetValue(str(egre))
		self.frame.tc_total.SetValue(str(ttal))

	def Aceptar(self):
		self.mdlCaj.ccam_anio = self.infoCaja['campAnio']
		self.mdlCaj.ccam_num = self.infoCaja['campNum']
		self.mdlCaj.caj_numero = self.infoCaja['numero']
		self.mdlCaj.close()

		mdlRep = ModeloReportes(self.infoCaja)
		nomArch = '/Reporte de caja del %s.xls' % (datetime.today().strftime("%d-%m-%Y"))
		mdlRep.dir = self.frame.tc_dir.GetValue() + nomArch
		try:
			mdlRep.generar_libro()
			wx.MessageBox("Reporte generado exitosamente", "Enhorabuena")
		except:
			wx.MessageBox("No se ha podido generar el reporte", "Ups!")


	"Eventos de ventana"
	def Buscar(self, event):
		dialog = wx.DirDialog(self.frame, "SELECCIONAR CARPETA DE DESTINO:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
		rta = dialog.ShowModal()
		if rta == wx.ID_OK:
			self.frame.tc_dir.SetValue(dialog.GetPath())
		dialog.Destroy()
