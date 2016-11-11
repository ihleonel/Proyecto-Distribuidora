# -*- coding:utf-8 -*-
import wx
from vistas.frame_modificar_campania import FrameModificarCampania
from modelos.modelCampanias import ModeloCampanias
from validadores.validarNumerico import ValidarFlotante, ValidarEntero

class ControladorModificarCampania:
	mdlCamp = ModeloCampanias()

	def __init__(self, parent, camp):
		self.parent = parent
		self.aCamp = camp

	def run(self):
		self.frame = FrameModificarCampania(self.parent)
		self.cargarDatos()
		self.cargarValidadores()
		self.frame.btn_cancelar.SetFocus()
		rpta = self.frame.ShowModal()
		if rpta == wx.ID_OK:
			self.Modificar()
		self.frame.Destroy()

	def cargarValidadores(self):
		self.frame.tc_diferencia.SetValidator(ValidarFlotante())
		self.frame.tc_base.SetValidator(ValidarFlotante())
		self.frame.tc_parametro.SetValidator(ValidarFlotante())

	def cargarDatos(self):
		self.frame.tc_fecha_inicio.SetValue(str(self.aCamp['inicio']))
		self.frame.tc_numero.SetValue(str(self.aCamp['numero']))
		self.frame.tc_ini_reparto.SetValue(self.aCamp['ini_reparto'])
		self.frame.tc_fin_reparto.SetValue(self.aCamp['fin_reparto'])
		self.frame.tc_diferencia.SetValue(str(self.aCamp['diferencia']))
		self.frame.tc_parametro.SetValue(str(self.aCamp['parametro']))
		self.frame.tc_base.SetValue(str(self.aCamp['base']))
		self.frame.tc_comentarios.SetValue(str(self.aCamp['comentarios']))

	def Modificar(self):
		self.mdlCamp.anio = self.aCamp['anio']
		self.mdlCamp.num = self.aCamp['numero']
		self.mdlCamp.ini_reparto = self.frame.tc_ini_reparto.GetValue()
		self.mdlCamp.fin_reparto = self.frame.tc_fin_reparto.GetValue()
		self.mdlCamp.diferencia = float(self.frame.tc_diferencia.GetValue())
		self.mdlCamp.parametro = float(self.frame.tc_parametro.GetValue())
		self.mdlCamp.base = float(self.frame.tc_base.GetValue())
		self.mdlCamp.comentario = self.frame.tc_comentarios.GetValue()
		self.mdlCamp.update()
