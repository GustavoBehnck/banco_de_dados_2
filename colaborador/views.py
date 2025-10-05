from django.shortcuts import render

from . import forms as colaborador_forms
from django_tables2 import SingleTableView
from .models import Client, Contract, Maintenance, Vehicle, VehicleModel
from .tables import ClientTable, ContractTable, MaintenanceTable, VehicleModelTable, VehicleTable


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
    template_name = "colaborador/list.html"


class VehicleListView(SingleTableView):
    model = Vehicle
    table_class = VehicleTable
    template_name = "colaborador/list.html"


class VehicleModelListView(SingleTableView):
    model = VehicleModel
    table_class = VehicleModelTable
    template_name = "colaborador/list.html"


class MaintenanceListView(SingleTableView):
    model = Maintenance
    table_class = MaintenanceTable
    template_name = "colaborador/list.html"


class ContractListView(SingleTableView):
    model = Contract
    table_class = ContractTable
    template_name = "colaborador/list.html"
