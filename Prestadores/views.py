from django.shortcuts import render

# Create your views here.
from Prestadores.models import Departamentos, SedesPrestador


def registroPrestadores(request):
    contexto={
        'departamentos':Departamentos.objects.all().order_by('nombre'),
        'prestadores':SedesPrestador.objects.all().order_by('nombre_prestador'),

    }
    return render(request,'',contexto)