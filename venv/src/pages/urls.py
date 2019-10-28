from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.urls import include
from django.contrib.auth import views as auth_views

from django.views.generic.base import RedirectView

urlpatterns = [
    path('empresa/create/', views.EmpresaCreate.as_view(), name='empresa_create'),
    path('empresa/list/', views.EmpresaListView.as_view(), name='empresa_list'),
    path('empresa/detail/', views.EmpresaDetailView.as_view(), name='empresa_detail'),
]