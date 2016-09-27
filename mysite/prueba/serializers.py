from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Usuario
		fields = ('id', 'nombre', 'apellido')


class UniversidadSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Universidad
		fields = ('id', 'nombre','direccion','aprobado')


class CompaneroSerializer(serializers.HyperlinkedModelSerializer):
	id_usuario_uno = UsuarioSerializer(read_only=True,allow_null=False)
	id_usuario_dos = UsuarioSerializer(read_only=True,allow_null=False)
	id_universidad = UniversidadSerializer(read_only=True,allow_null=False)

	class Meta:
		model = Companero
		fields = ('id', 'id_usuario_uno','id_usuario_dos','id_universidad')