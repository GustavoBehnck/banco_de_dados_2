import django_tables2 as tables
from .models import Client, Vehicle

class ClientTable(tables.Table):
    edit = tables.TemplateColumn(
        '<a href="{% url \'home\' %}" class="btn btn-sm btn-primary">Editar</a>',
        orderable=False,
        verbose_name='Ações'
    )

    class Meta:
        model = Client
        template_name = "django_tables2/bootstrap5-responsive-custom.html"
        fields = ("id", "trade_name", "company_name", "cnpj", "status")

class VehicleTable(tables.Table):
    edit = tables.TemplateColumn(
        '<a href="{% url \'home\' %}" class="btn btn-sm btn-primary">Editar</a>',
        orderable=False,
        verbose_name='Ações'
    )

    class Meta:
        model = Vehicle
        template_name = "django_tables2/bootstrap5-responsive-custom.html"
        fields = ("model", "chassis", "status", "observation")
