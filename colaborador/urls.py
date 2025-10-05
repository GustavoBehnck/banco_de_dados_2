"""
URL configuration for graomestre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.home, name="colaborador_home"),
    path("clientes/", views.ClientListView.as_view(), name="colaborador_client_list"),
    path("clientes/cadastrar", views.new_client, name="colaborador_new_client"),
    path("veiculos/modelos/cadastrar", views.new_vehicle_model, name="colaborador_new_vehicle_model"),
    path("veiculos/cadastrar", views.new_vehicle, name="colaborador_new_vehicle"),
    path("manutencoes/cadastrar", views.new_maintenence, name="colaborador_new_maintenence"),
    path("contratos/cadastrar", views.new_contract, name="colaborador_new_contract"),
]
