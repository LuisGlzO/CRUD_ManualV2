from django.db import models

# Create your models here.
class Salones(models.Model):
    #id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 30)
    edificio = models.CharField(max_length = 30)
    capacidad = models.PositiveIntegerField()
    
    def _str_(self):
        return self.nombre

class Persona(models.Model):
    #id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 200)
    salonAsignado = models.ForeignKey(Salones, on_delete=models.CASCADE, null = True, blank = True, default=None)

    def __str__(self):
        persona = self.nombre + self.apellido
        return persona


