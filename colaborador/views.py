from django.shortcuts import render

def cadastrar_modelo(request):
    return render(request, "colaborador/cadastrar_modelo.html")
