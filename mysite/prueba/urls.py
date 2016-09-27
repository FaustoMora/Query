from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from tastypie.api import Api
from rest_framework import routers
from .api import *
from .api_views import *

v1_api = Api(api_name='v1')
v1_api.register(UsuarioResource())
v1_api.register(UniversidadResource())
v1_api.register(CompaneroResource())

## rest_framework urls
router = routers.DefaultRouter()
router.register(r'rest/usuario', UsuarioViewSet)
router.register(r'rest/universidad', UniversidadViewSet)
router.register(r'rest/companero', CompaneroViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^pag[/]?$',views.pagina,name='pagina'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^', include(router.urls)),
]

