#from django.shortcuts import render
#from django.http import HttpResponse 
# Create your views here.
"""
def holamundo(request):
    return HttpResponse ("Respuesta funcion")
"""

from django.shortcuts import render 
from django.http import HttpResponse
from django.views import generic

# Importa las clases definidas en el modelo
from .models import Arboles_sembrados, Coordenadas, Departamento, Municipio, Especie

# Create your views here.
def index(request): # Genera contadores de algunos de los objetos principales
    num_Arboles_sembrados = Arboles_sembrados.objects.all().count()
    num_Coordenadas= Coordenadas.objects.all().count()
    num_Departamento = Departamento.objects.all().count() 
    num_municipio= Municipio.objects.all().count()
    num_Especie = Especie.objects.all().count()

# Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context=
    {'num_Arboles_sembrados':num_Arboles_sembrados,'num_Coordenadas':num_Coordenadas, 
     'num_Departamento': num_Departamento, 'num_Municipio': num_municipio, 'num_Especie': num_Especie,},
    )
