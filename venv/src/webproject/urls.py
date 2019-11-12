"""webproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from pages.views import home_view
from users.views import user_create_view, user_login_view
from pages.views import *

urlpatterns = [
    path('', home_view, name='home'),
    #path('login/', user_login_view, name='login'),
    path('register/', user_create_view),
    path('admin/', admin.site.urls),
    path('', include("pages.urls")), # Registration views.
    path('', include("django.contrib.auth.urls")), # Registration views.
    path('empresas/', empresa_view),
    path('empresas_registrar/', empresa_create_view),
    path('empresas_modificar/', empresa_modify_view),
    path('rutas/', ruta_view),
    path('rutas_registrar/', ruta_create_view),
    path('rutas_modificar/', ruta_modify_view),
    path('paradas/', parada_view),
    path('paradas_registrar/', parada_create_view),
    path('paradas_modificar/', parada_modify_view),
    path('perfil/', profile_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




""" urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
] """