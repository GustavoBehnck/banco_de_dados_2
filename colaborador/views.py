from django.shortcuts import render

from .forms import ContactForm

def index(request):
    form = ContactForm(request.POST or None)
    return render(request, "colaborador/index.html", {'form': form})

def about(request):
    return render(request, "colaborador/about.html")

def contact(request):
    form = ContactForm(request.POST or None)
    return render(request, "colaborador/contact.html", {'form': form})