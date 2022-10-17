from django.db import models

# Create your models here.
from django.db import models



# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    #Hay una herencia en estas clases, tomando la clase
    #de models importado de django.
    def __str__(self):
        return f"Nombre:{self.nombre} - Apellido:{self.camada}"
   
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre:{self.nombre} - Apellido:{self.apellido} - Email: {self.email}"
    #Agregar este método en la clase, me permite definir una forma de mostrar para
    #ésta clase, un orden y formato de los atributos que la componen. Así, no veré un
    #objeto Estudiante desde la web, sino que veré la información contenida.

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre:{self.nombre} - Apellido:{self.apellido} - Email: {self.email} - Profesión: {self.profesion}"
   

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregada = models.BooleanField()

    def __str__(self):
        return f"Nombre:{self.nombre} - Fecha de Entrega:{self.fechaDeEntrega} - Entregada: {self.entregada}"
 


class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    relación = models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField()
    Edad = models.IntegerField()

    def __str__(self):
        return f"Nombre:{self.nombre} - Relación:{self.relación} - Fecha de Nacimiento: {self.fechaDeNacimiento} - Edad: {self.Edad}"
 