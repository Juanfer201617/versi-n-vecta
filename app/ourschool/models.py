from django.db import models

# Create your models here.
from django.db import models
from django.shortcuts import render


# Create your models here.

class Usuario(models.Model):
    ROLES = (
        (1, "admin"),
        (2, "estudiante"),
        (3, "docente")
    )
    nombre_apellido = models.CharField(max_length=30)
    tipo_documento = models.CharField(max_length=30)
    numero_documento = models.CharField(max_length=30, default=0)
    telefono = models.IntegerField(default=0)
    correo = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(default=0)
    contrasena = models.CharField(max_length=30)
    rol = models.IntegerField(choices=ROLES)

    def __str__(self):
        return f"{self.nombre_apellido}"



class asesoria(models.Model):
    materia = models.CharField(max_length=30)
    grado = models.IntegerField()
    duracion = models.CharField(max_length=30)
    reseñas = models.CharField(max_length=30)


def __str__(self):
    return f"{self.materia}"



class pagos(models.Model):
    estado = models.CharField(max_length=30)
    valor = models.IntegerField()


def __str__(self):
    return f"{self.estado}"