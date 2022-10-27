from django.db import models
from django.contrib.auth.models import User

# Create your models here.




# Create your models here.

class Cocinero(models.Model):
    imagen = models.ImageField(upload_to= "cocineros", null= True, blank = True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()
    Experiencia = models.CharField(max_length=4000)
    #Hay una herencia en estas clases, tomando la clase
    #de models importado de django.
    def __str__(self):
        return f" - Nombre:{self.nombre} - Apellido:{self.apellido} - Edad: {self.edad} - Email: {self.email} - Experiencia: {self.Experiencia}"
   
class Comentario(models.Model):
    Comentario = models.CharField(max_length=500)
    us = models.CharField(max_length=500, null=True, blank=True)
    autor = models.CharField(max_length=500, null=True, blank=True)
    nivel = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"Comentario: {self.Comentario} - Usuario: {self.us}"
    #Agregar este método en la clase, me permite definir una forma de mostrar para
    #ésta clase, un orden y formato de los atributos que la componen. Así, no veré un
    #objeto Estudiante desde la web, sino que veré la información contenida.

class Receta(models.Model):
    imagen = models.ImageField(upload_to= "recetas", null= True, blank = True)   
    nombre = models.CharField(max_length=80)
    ingrediente = models.CharField(max_length=5000, null=True, blank = True)
    texto = models.CharField(max_length=5000)
    email = models.EmailField()
    autor = models.CharField(max_length=30)

    def __str__(self):
        return f"- \n Receta: {self.nombre} - \n Instrucciones: {self.texto} - \n Email de contacto: {self.email} - \n Autor: {self.autor}"
    

class Imagen(models.Model):
    imagen = models.ImageField(null= True, blank = True)


class Avatar(models.Model):
     user = models.ForeignKey(User, on_delete = models.CASCADE)
     #El foreignkey viene de conceptos de base de datos, relaciona dos tablas,
     #cada usuario tendrá una tabla, y no más, las vincula. El on_delete
     # implica que al eliminar un usuario, también se eliminará el avatar, no puede existir uno
     #sin el otro.
     image = models.ImageField(upload_to="avatares", null= True, blank = True )
     #Si no le aclaro que puede ser nulo, no podré migrar el modelo.


class Receta_Amateur(models.Model):  
    nombre = models.CharField(max_length=80)
    ingrediente = models.CharField(max_length=5000, null=True, blank = True)
    texto = models.CharField(max_length=5000)
    autor = models.CharField(max_length=30)
    fecha = models.DateTimeField(auto_now_add=True)
    us = models.CharField(max_length=30,null=True, blank=True)
    nivel = 'amateur'