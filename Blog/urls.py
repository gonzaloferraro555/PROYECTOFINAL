from django.urls import path
from Blog.views import *    



urlpatterns = [
    path('', inicio),
    path('home/', home),
    path('contacto/', contacto),
    path('recetas/', recetas),
    path('arroz/', arroz),
    path('camaron/', camaron),
    path('cuatroquesos/',cuatroquesos),
    path('hamburguesa/', hamburguesa),
    path('panceta/', panceta),
    path('pechuga/', pechuga),
    path('steak/', steak),
    path('taco/', taco),
]