from django.shortcuts import render

from . import forms as colaborador_forms
from django_tables2 import SingleTableView
from .models import Client
from .tables import ClientTable


def home(request):
    return render(request, "colaborador/home.html")


def new_client(request):
    form = colaborador_forms.NewClientForm()
    return render(request, "colaborador/form.html", {"form": form})


def new_vehicle_model(request):
    form = colaborador_forms.NewVehicleModelForm()
    return render(request, "colaborador/form.html", {"form": form})


def new_vehicle(request):
    form = colaborador_forms.NewVehicleForm()
    return render(request, "colaborador/form.html", {"form": form})


def new_maintenence(request):
    form = colaborador_forms.NewMaintenanceForm()
    return render(request, "colaborador/form.html", {"form": form})


def new_contract(request):
    form = colaborador_forms.NewContractForm()
    return render(request, "colaborador/form.html", {"form": form})


class ClientListView(SingleTableView):
    model = Client
    table_class = ClientTable
    template_name = "colaborador/client_list.html"
