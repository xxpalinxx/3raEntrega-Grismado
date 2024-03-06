from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.apellido}, {self.nombre} -- Edad: {self.edad}"

class Proyectos(models.Model):
    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    comercial = models.CharField(max_length=60)

    def __str__(self):
        return f"Nombre: {self.nombre} -- Tipo: {self.tipo}" if self.comercial == True +"Comercial" else "Residencial"

class Consulta(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    consulta = models.CharField(max_length=200)

    def __str__(self):
        return f"Nombre:{self.nombre} -- {self.email}"
