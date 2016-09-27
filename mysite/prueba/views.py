import pprint
import json
from django.shortcuts import render
from .models import *
from django.core.serializers import serialize
from .api import * 
from .serializers import *
from .api_views import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.

def pagina(request):
	compa = Companero.objects.select_related('id_usuario_uno__nombre','id_usuario_dos__nombre','id_universidad__nombre').first()
	#print type(compa)
	compas = Companero.objects.select_related('id_usuario_uno__nombre','id_usuario_dos__nombre','id_universidad__nombre')
	#compas2 = Companero.objects.select_related('id_usuario_uno__nombre','id_usuario_dos__nombre','id_universidad__nombre').only('id_companero','id_usuario_uno__nombre','id_usuario_dos__nombre','id_universidad__nombre')
	compas2 = Companero.objects.select_related('id_usuario_uno__nombre','id_usuario_dos__nombre','id_universidad__nombre')
	print compas2.query
	compa2 = compas2.first()
	data2 = None

	data = serialize('json', [ compa2, ],indent=2,use_natural_foreign_keys=True, use_natural_primary_keys=True)
	print data
	print type(data)

	json_data = json.dumps(data)
	print type(json_data)

	#############################################################

	comp = CompaneroResource()
	request_bundle = comp.build_bundle(request=request)
	cm = comp.obj_get(request_bundle, pk=1)

	cm_bundle = comp.build_bundle(request=request, obj=cm)
	data3 = comp.serialize(None, comp.full_dehydrate(cm_bundle), "application/json")
	print data3
	print type(data3)

	# bloque mysql para la operacion
	# select c.id, c.usuario_uno, c.usuario_dos, c.universidad, u.nombre,
	# u.direccion, u.aprobado, us.nombre, us.apellido, uss.nombre, uss.apellido 
	# from companero c 
	# inner join usuario us on (c.usuario_uno = us.id )
	# inner join usuario uss on (c.usuario_dos = uss.id )
	# inner join universidad u on (c.universidad = u.id );

	print 'usando raw'
	query = 'select c.id, c.id_usuario_uno_id, c.id_usuario_dos_id, c.id_universidad_id, u.nombre, u.direccion, u.aprobado, us.nombre, us.apellido, uss.nombre, uss.apellido from Companero c inner join Usuario us on (c.id_usuario_uno_id = us.id ) inner join Usuario uss on (c.id_usuario_dos_id = uss.id ) inner join Universidad u on (c.id_universidad_id = u.id )'
	#query = query = 'select * from Companero c inner join Usuario us on (c.id_usuario_uno = us.id ) inner join Usuario uss on (c.id_usuario_dos = uss.id ) inner join Universidad u on (c.id_universidad = u.id )'

	data2 = Companero.objects.raw(query)
	for obj in data2:
		print obj.get_json()


	## usando django rest_framework
	data4 = Companero.objects.get(id=1)
	data4 = CompaneroSerializer(data4)
	data4 = JSONRenderer().render(data4.data)
	print data4



	return render(request,'pagina.html',{'objeto':data,'objeto2':data2,'objeto3':data3,'objeto4':data4})


def home(request):
	return render(request,'home.html')
