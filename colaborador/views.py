from django.shortcuts import render

from .forms import ContactForm

def index(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # process form data
        print(form.cleaned_data)
    return render(request, "colaborador/index.html", {'form': form})
