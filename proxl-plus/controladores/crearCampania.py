# -*- coding : utf-8 -*-
import wx, time
from vistas.frame_crear_campania import FrameCrearCampania
from modelos.modelCampanias import ModeloCampanias
from validadores.validador import Validar
from validadores.validarNumerico import ValidarFlotante, ValidarEntero

class ControladorCrearCampania:
	mdlCamp = ModeloCampanias()
	def __init__(self, parent, usuario):
		self.usuario = usuario
		self.parent = parent

	def run(self):
		self.frame = FrameCrearCampania(self.parent)
		self.frame.tc_comentario.SetFocus()
		self.cargarDatos()
		self.cargarValidadores()
		resp = self.frame.ShowModal()
		if resp == wx.ID_OK:
			self.AgregarCampania()

	def cargarValidadores(self):
		self.mdlCamp.anio = int(time.strftime("%Y"))
		self.frame.tc_numero.SetValidator(Validar())
		self.frame.tc_diferencia.SetValidator(ValidarFlotante())
		self.frame.tc_base.SetValidator(ValidarFlotante())
		self.frame.tc_parametro.SetValidator(ValidarFlotante())

	def cargarDatos(self):
		self.mdlCamp.anio = int(time.strftime("%Y"))
		n = self.mdlCamp.get_next_number_campaign()
		self.frame.tc_numero.SetValue(str(n))
		self.frame.tc_fecha_inicio.SetValue(time.strftime("%d-%m-%Y"))
		self.frame.tc_usuario.SetValue(self.usuario)

	def AgregarCampania(self):
		self.mdlCamp.anio = int(time.strftime("%Y"))
		self.mdlCamp.num = int(self.frame.tc_numero.GetValue())
		if not self.mdlCamp.exist_campaign():
			self.mdlCamp.inicio = time.strftime("%Y-%m-%d")
			self.mdlCamp.ini_repato = self.frame.tc_ini_reparto.GetValue()
			self.mdlCamp.diferencia = float(self.frame.tc_diferencia.GetValue())
			self.mdlCamp.parametro = float(self.frame.tc_parametro.GetValue())
			self.mdlCamp.base = float(self.frame.tc_base.GetValue())
			self.mdlCamp.comentario = self.frame.tc_comentario.GetValue()
			self.mdlCamp.usuario = self.usuario
			self.mdlCamp.create()
		else:
			wx.MessageBox(u"La campana que desea crear ya existe.", "Ups!")