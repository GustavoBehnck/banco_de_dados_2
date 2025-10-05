from django.shortcuts import render

from .forms import ContactForm

def index(request):
    form = ContactForm(request.POST or None)
    return render(request, "home/index.html", {'form': form})

def about(request):
    return render(request, "home/about.html")

def contact(request):
    form = ContactForm(request.POST or None)
    return render(request, "home/contact.html", {'form': form})

def cadastrar_modelo(request):
    form = ContactForm(request.POST or None)
    return render(request, "colaborador/cadastrar_modelo.html", {'form': form})
