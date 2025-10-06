from django.shortcuts import get_object_or_404, render

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


def edit_client(request, id):
    client = get_object_or_404(Client, id=id)
    form = colaborador_forms.EditClientForm(instance=client)
    return render(request, "colaborador/form.html", {"form": form})


def edit_vehicle_model(request, id):
    vehicle_model = get_object_or_404(VehicleModel, id=id)
    form = colaborador_forms.EditVehicleModelForm(instance=vehicle_model)
    return render(request, "colaborador/form.html", {"form": form})


def edit_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    form = colaborador_forms.EditVehicleForm(instance=vehicle)
    return render(request, "colaborador/form.html", {"form": form})


def edit_maintenence(request, id):
    maintenance = get_object_or_404(Maintenance, id=id)
    form = colaborador_forms.EditMaintenanceForm(instance=maintenance)
    return render(request, "colaborador/form.html", {"form": form})


def edit_contract(request, id):
    contract = get_object_or_404(Contract, id=id)
    form = colaborador_forms.EditContractForm(instance=contract)
    return render(request, "colaborador/form.html", {"form": form})