from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import *
from .models import *


class UsuarioViewSet(viewsets.ModelViewSet):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer


class UniversidadViewSet(viewsets.ModelViewSet):
	queryset = Universidad.objects.all()
	serializer_class = UniversidadSerializer


class CompaneroViewSet(viewsets.ModelViewSet):
	queryset = Companero.objects.all()
	serializer_class = CompaneroSerializer


class CompaneroAPIView(APIView):
	
	def get(self, request, pk, format=None):
		comp = self.get_object(pk)
		comp = CompaneroSerializer(comp)
		return Response(comp.data)