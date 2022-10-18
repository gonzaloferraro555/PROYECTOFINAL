from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request,"inicio.html")
# Create your views here.

def home(request):
    return render(request,"home.html")
# Create your views here.

def contacto(request):
    return render(request,"contacto.html")