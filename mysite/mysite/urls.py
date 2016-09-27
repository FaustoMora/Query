from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^',include('prueba.urls')),
    url(r'^$', 'prueba.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
