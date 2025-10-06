import django_tables2 as tables
from .models import Client, Contract, Maintenance, Vehicle, VehicleModel

class ClientTable(tables.Table):
    edit = tables.TemplateColumn(
        '<a href="{% url \'colaborador_edit_client\' record.id %}" class="btn btn-sm btn-primary">Editar</a> '
        '<a href="{% url \'colaborador_edit_client\' record.id %}" class="btn btn-sm btn-outline-primary">Ver detalhes</a>',
        orderable=False,
        verbose_name='Ações'
    )

    class Meta:
        model = Client
        template_name = "django_tables2/bootstrap5-responsive-custom.html"
        fields = ("id", "trade_name", "company_name", "cnpj", "status")


class VehicleTable(tables.Table):
    edit = tables.TemplateColumn(
        '<a href="{% url \'colaborador_edit_vehicle\' record.id %}" class="btn btn-sm btn-primary">Editar</a>',
        orderable=False,
        verbose_name='Ações'
    )

    class Meta:
        model = Vehicle
        template_name = "django_tables2/bootstrap5-responsive-custom.html"
        fields = ("model", "chassis", "status", "observation")


class VehicleModelTable(tables.Table):
    edit = tables.TemplateColumn(
        '<a href="{% url \'colaborador_edit_vehicle_model\' record.id %}" class="btn btn-sm btn-primary">Editar</a>',
        orderable=False,
        verbose_name='Ações'
    )

    class Meta:
        model = VehicleModel
        template_name = "django_tables2/bootstrap5-responsive-custom.html"
        fields = ("type", "fabrication_year", "battery_capacity", "charging_time")
        order_by = ("-fabrication_year", "type")


class MaintenanceTable(tables.Table):
    edit = tables.TemplateColumn(
        '<a href="{% url \'colaborador_edit_maintenence\' record.id  %}" class="btn btn-sm btn-primary">Editar</a>',
        orderable=False,
        verbose_name='Ações'
    )

    class Meta:
        model = Maintenance
        template_name = "django_tables2/bootstrap5-responsive-custom.html"
        fields = ("date", "vehicle", "link_to_ticket", "reason")
        order_by = ("date", "vehicle")


class ContractTable(tables.Table):
    edit = tables.TemplateColumn(
        '<a href="{% url \'colaborador_edit_contract\' record.id %}" class="btn btn-sm btn-primary">Editar</a> '
        '<a href="{% url \'colaborador_edit_contract\' record.id %}" class="btn btn-sm btn-outline-primary">Ver detalhes</a>',
        orderable=False,
        verbose_name='Ações'
    )

    class Meta:
        model = Contract
        template_name = "django_tables2/bootstrap5-responsive-custom.html"
        fields = ("client", "status", "start_date", "end_date")
