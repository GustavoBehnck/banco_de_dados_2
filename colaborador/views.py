from django.shortcuts import render

from colaborador.forms import NewClientForm

def home(request):
    return render(request, "colaborador/home.html")

def new_client(request):
    form = NewClientForm()
    return render(request, "colaborador/form.html", {"form": form})
