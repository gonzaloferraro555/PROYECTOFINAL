from django.urls import path
from Blog.views import *    



urlpatterns = [
    path('', inicio),
    path('home/', home),
    path('contacto/', contacto),
]