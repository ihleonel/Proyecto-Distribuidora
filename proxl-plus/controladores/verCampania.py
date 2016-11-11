# -*- coding:utf-8 -*-
import wx
from vistas.frame_ver_campania import FrameVerCampania
from modelos.modelCampanias import ModeloCampanias
class ControladorVerCampania:
	mdlCampania = ModeloCampanias()

	def __init__(self, parent, Seleccionado):
		self.parent = parent
		self.mdlCampania.num = Seleccionado[1]
		self.mdlCampania.inicio = Seleccionado[0]

	def run(self):
		self.frame = FrameVerCampania(self.parent)
		self.cargarDatos()
		self.frame.ShowModal()

	def capturarEventos(self):
		pass

	def cargarDatos(self):
		datos = self.mdlCampania.read()
		camp = str(datos[0][1])+"-"+str(datos[0][2]).split("-")[0]
		self.frame.tc_campania.SetValue(camp)
		self.frame.tc_inicio.SetValue(str(datos[0][2]))
		self.frame.tc_fin.SetValue(str(datos[0][3]))
		self.frame.tc_comentarios.SetValue(str(datos[0][4]))
		self.frame.tc_usuario.SetValue(str(datos[0][5]))
