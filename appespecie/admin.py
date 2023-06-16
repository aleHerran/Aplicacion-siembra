from django.contrib import admin

# Register your models here.}

from .models import Arboles_sembrados, Coordenadas, Departamento, Municipio, Especie
admin.site.register(Arboles_sembrados)
admin.site.register(Coordenadas)
admin.site.register(Municipio)
admin.site.register(Especie)
