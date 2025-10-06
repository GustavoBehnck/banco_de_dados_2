from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, HTML

from .models import Client, Contract, Maintenance, Vehicle, VehicleModel

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-6'),
                Column('email', css_class='col-md-6'),
            ),
            'message',
            Submit('submit', 'Send Message', css_class='btn btn-primary')
        )

class NewClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["cnpj", "trade_name", "company_name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("<h2>Cadastrar cliente</h2>"),
            *self.fields,
            Submit("submit", "Cadastrar"),
        )


class EditClientForm(NewClientForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            HTML("<h2>Editar cliente</h2>"),
            *self.fields,
            Submit("submit", "Editar"),
        )


class NewVehicleModelForm(forms.ModelForm):
    class Meta:
        model = VehicleModel
        fields = [
            "type",
            "battery_capacity",
            "fabrication_year",
            "charging_time",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("<h2>Cadastrar modelo de veículo</h2>"),
            *self.fields,
            Submit("submit", "Cadastrar"),
        )


class EditVehicleModelForm(NewVehicleModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            HTML("<h2>Editar modelo de veículo</h2>"),
            *self.fields,
            Submit("submit", "Editar"),
        )


class NewVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            "chassis",
            "model",
            "observation",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("<h2>Cadastrar veículo</h2>"),
            *self.fields,
            Submit("submit", "Cadastrar"),
        )


class EditVehicleForm(NewVehicleForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            HTML("<h2>Editar veículo</h2>"),
            *self.fields,
            Submit("submit", "Editar"),
        )



class NewMaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = [
            "vehicle",
            "date",
            "reason",
            "link_to_ticket",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("<h2>Cadastrar manutenção</h2>"),
            *self.fields,
            Submit("submit", "Cadastrar"),
        )


class EditMaintenanceForm(NewMaintenanceForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            HTML("<h2>Editar manutenção</h2>"),
            *self.fields,
            Submit("submit", "Editar"),
        )


class NewContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            "client",
            "start_date",
            "end_date",
            "lease_deed",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML("<h2>Cadastrar contrato</h2>"),
            *self.fields,
            Submit("submit", "Cadastrar"),
        )


class EditContractForm(NewContractForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper.layout = Layout(
            HTML("<h2>Editar contrato</h2>"),
            *self.fields,
            Submit("submit", "Editar"),
        )
