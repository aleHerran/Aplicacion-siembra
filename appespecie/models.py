from django.db import models
from django.urls import reverse
from django.apps import AppConfig
from django.conf import settings


# Create your models here.
class Arboles_sembrados (models.Model):
    id = models.BigIntegerField(primary_key=True, max_length=255)
    fecha_siembra = models.DateField('dd-mm-yyyy')
    cantidad=models.BigIntegerField(max_length=255)

# Metodo que devuelve el campo que se desea mostrar en la pagina para acceder al registro.
    def __str__(self):
        return (str(self.id))

# Metodo que devuelve la url para acceder a una instancia particular del modelo.
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

class Departamento (models.Model):
    nombre= models.CharField(primary_key=True, max_length=255)
    

class Municipio (models.Model):
    nombre= models.CharField(primary_key=True, max_length=255)
    Departamento_nombre = models.ForeignKey(Departamento,on_delete=models.SET_NULL, null=True)


    
class Especie (models.Model):
    nombre_cientifico= models.CharField(primary_key=True, max_length=255) 
    nombre_común = models.CharField(max_length=255)
    

class Coordenadas (models.Model):
    id = models.BigIntegerField(primary_key=True)
    longitud = models.BigIntegerField(max_length=255)
    latitud = models.BigIntegerField(max_length=255)


