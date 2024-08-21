from django.db import models

class Nutricionista(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    matricula = models.CharField(max_length=8)

class Paciente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    descripcion = models.TextField()

class Sesion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nutricionista = models.ForeignKey(Nutricionista, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
