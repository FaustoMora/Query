from tastypie import fields
from tastypie.resources import ModelResource
from .models import *


class UsuarioResource(ModelResource):
	class Meta:
		queryset = Usuario.objects.all()
		resource_name = 'usuario'
		allowed_methods = ['get']

class UniversidadResource(ModelResource):
	class Meta:
		queryset = Universidad.objects.all()
		resource_name = 'universidad'
		allowed_methods = ['get']


class CompaneroResource(ModelResource):
	usuario_uno = fields.ForeignKey(UsuarioResource, 'id_usuario_uno',full=True)
	usuario_dos = fields.ForeignKey(UsuarioResource, 'id_usuario_dos',full=True)
	universidad = fields.ForeignKey(UniversidadResource, 'id_universidad',full=True)

	class Meta:
		queryset = Companero.objects.all()
		resource_name = 'companero'
		allowed_methods = ['get']