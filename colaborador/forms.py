from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, HTML

from .models import Client

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
            HTML("<h2>Cadastrar novo cliente</h2>"),
            *self.fields,
            Submit("submit", "Cadastrar"),
        )