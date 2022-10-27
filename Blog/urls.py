from django.urls import path
from Blog.views import *
from django.contrib.auth.views import LogoutView    



urlpatterns = [
    path('', inicio),
    path('home/', home),
    path('contacto/', contacto),
    path('nosotros/', nosotros),
    path('recetas/', recetas),
    path('arroz/', arroz),
    path('camaron/', camaron),
    path('cuatroquesos/',cuatroquesos),
    path('hamburguesa/', hamburguesa),
    path('panceta/', panceta),
    path('pechuga/', pechuga),
    path('steak/', steak),
    path('taco/', taco),
    path('login/', login_request),
    path('registro/', register),
    path('perfil/', perfilView),
    path('perfil/editar_perfil', editar_perfil),
    path('perfil/agregarAvatar/', AgregarAvatar),
    path('perfil/changepass/', changepass),
    path('editar_arroz/<com_id>', editar_comentario_arroz),
    path('editar_camaron/<com_id>', editar_comentario_camaron),
    path('editar_hamburguesa/<com_id>', editar_comentario_hamburguesa),
    path('editar_panceta/<com_id>', editar_comentario_panceta),
    path('editar_pechuga/<com_id>', editar_comentario_pechuga),
    path('editar_steak/<com_id>', editar_comentario_steak),
    path('editar_taco/<com_id>', editar_comentario_taco),
    path('editar_cuatroquesos/<com_id>', editar_comentario_cuatroquesos),
    path('editar_tus_recetas/<r_id>', editar_recetas_amateur),
    path('eliminar/<com_id>', eliminar_comentario),
    path('eliminar_tus_recetas/<id>', eliminar_tus_recetas),
    path('tus_recetas/', tus_recetas),
    path('agregar_receta/', agregar_receta),
    path('logout/', LogoutView.as_view(template_name = "inicio.html"), name= "Logout"),
]