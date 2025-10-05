from django.shortcuts import render

from .forms import ContactForm

def home(request):
    form = ContactForm(request.POST or None)
    return render(request, "home/home.html", {'form': form})

def about(request):
    return render(request, "home/about.html")

def contact(request):
    form = ContactForm(request.POST or None)
    return render(request, "home/contact.html", {'form': form})
