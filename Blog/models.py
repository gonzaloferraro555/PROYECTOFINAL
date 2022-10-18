from django.db import models

# Create your models here.
from django.db import models



# Create your models here.
class Cocinero(models.Model):
    imagen = models.ImageField()
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()
    Experiencia = models.CharField(max_length=4000)
    #Hay una herencia en estas clases, tomando la clase
    #de models importado de django.
    def __str__(self):
        return f"Foto:{self.imagen} - Nombre:{self.nombre} - Apellido:{self.apellid} - Edad: {self.edad} - Email: {self.email} - Experiencia: {self.Experiencia}"
   
class Comentario(models.Model):
    texto = models.CharField(max_length=500)
    NombreYApellido = models.CharField(max_length=80)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre:{self.NombreYApellido} - Email: {self.email} - Texto:{self.texto} "
    #Agregar este método en la clase, me permite definir una forma de mostrar para
    #ésta clase, un orden y formato de los atributos que la componen. Así, no veré un
    #objeto Estudiante desde la web, sino que veré la información contenida.

class Receta(models.Model):
    imagen = models.ImageField()
    nombre = models.CharField(max_length=30)
    texto = models.CharField(max_length=800)
    email = models.EmailField()
    autor = models.CharField(max_length=30)

    def __str__(self):
        return f"Foto:{self.imagen} - Nombre:{self.nombre} - Texto:{self.texto} - Email: {self.email} - Autor: {self.autor}"
   

class Imagen(models.Model):
    imagen = models.ImageField()