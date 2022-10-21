from django.shortcuts import render
from Blog.models import *
# Create your views here.


def inicio(request):
    return render(request,"inicio.html")
# Create your views here.

def home(request):
    return render(request,"home.html")
# Create your views here.

def contacto(request):
    return render(request,"contacto.html")

def recetas(request):
    return render(request,"recetas.html")



def arroz(request):
    autor1 = "Martín Berasategui"
    rec = Receta.objects.filter(autor=autor1)
    if request.method == "POST":
        """estu = Estudiante(nombre = request.POST["Nombre"], apellido= request.POST["Apellido"]
        , email = request.POST["Email"])
        estu.save()
        estu = Estudiante.objects.all()
        return render(request, "estudiantes_CRUD/read_estudiante.html",{"estudiantes": estu} )
        #Devuelvo el read, para que me muestre nuevamente todos los estudiantes pero 
        #la listas actualizada."""
    else:
        return render(request, "arroz.html",{"recetas":rec})



def camaron(request):
    return render(request,"camaron.html")


def cuatroquesos(request):
    return render(request,"cuatroquesos.html")


def hamburguesa(request):
    return render(request,"hamburguesa.html")

def panceta(request):
    return render(request,"panceta.html")


def pechuga(request):
    return render(request,"pechuga.html")

def steak(request):
    return render(request,"steak.html")

def taco(request):
    return render(request,"taco.html")