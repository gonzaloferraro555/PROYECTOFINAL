from django.shortcuts import render
from Blog.models import *
# Create your views here.
from django.http import HttpResponse


#Necesito el responde y el render para mostrar los html.

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm,User
from django.contrib.auth import login, logout,authenticate, update_session_auth_hash
from Blog.forms import FormularioDeRegistro, AvatarFormulario,UserEditForm, ChangePasswordForm,form_comentario,form_receta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def inicio(request):
    return render(request,"inicio.html")
# Create your views here.

@login_required()
def home(request):
    avatar=Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'home.html',{'avatar':avatar})
# Create your views here.

def contacto(request):
    return render(request,"contacto.html")

def nosotros(request):
    return render(request,"nosotros.html")   
    
    

@login_required
def recetas(request):
    return render(request,"recetas.html")



def arroz(request):
    autor1 = "Martín Berasategui"
    rec = Receta.objects.filter(autor=autor1)
    com=Comentario.objects.filter(autor=autor1)
    if request.method == "POST":
        formulario = form_comentario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            com = Comentario(Comentario = informacion["Comentario"],
            us= request.user, autor="Martín Berasategui")
            com.save() #Guardo la data en la base de datos como en la función estudiantes.
            com=Comentario.objects.filter(autor=autor1)
            return render(request, "arroz.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        else:
            formulario = form_comentario()
            return render(request, "arroz.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        
    else:
        formulario = form_comentario()
        return render(request, "arroz.html",{"recetas":rec,"comentarios":com,"formulario":formulario})



def camaron(request):
    autor1 = "Daniel García"
    rec = Receta.objects.filter(autor=autor1)
    com=Comentario.objects.filter(autor=autor1)
    if request.method == "POST":
        formulario = form_comentario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            com = Comentario(Comentario = informacion["Comentario"],
            us= request.user, autor="Daniel García")
            com.save() #Guardo la data en la base de datos como en la función estudiantes.
            com=Comentario.objects.filter(autor=autor1)
            return render(request, "camaron.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        else:
            formulario = form_comentario()
            return render(request, "camaron.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        
    else:
        formulario = form_comentario()
        return render(request, "camaron.html",{"recetas":rec,"comentarios":com,"formulario":formulario})



def cuatroquesos(request):
    autor1 = "Nino Redruello en Fismuler"
    rec = Receta.objects.filter(autor=autor1)
    com=Comentario.objects.filter(autor=autor1)
    if request.method == "POST":
        formulario = form_comentario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            com = Comentario(Comentario = informacion["Comentario"],
            us= request.user, autor="Nino Redruello en Fismuler")
            com.save() #Guardo la data en la base de datos como en la función estudiantes.
            com=Comentario.objects.filter(autor=autor1)
            return render(request, "cuatroquesos.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        else:
            formulario = form_comentario()
            return render(request, "cuatroquesos.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        
    else:
        formulario = form_comentario()
        return render(request, "cuatroquesos.html",{"recetas":rec,"comentarios":com,"formulario":formulario})



def hamburguesa(request):
    autor1 = "Antonio Arrabal"
    rec = Receta.objects.filter(autor=autor1)
    com=Comentario.objects.filter(autor=autor1)
    if request.method == "POST":
        formulario = form_comentario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            com = Comentario(Comentario = informacion["Comentario"],
            us= request.user, autor="Antonio Arrabal")
            com.save() #Guardo la data en la base de datos como en la función estudiantes.
            com=Comentario.objects.filter(autor=autor1)
            return render(request, "hamburguesa.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        else:
            formulario = form_comentario()
            return render(request, "hamburguesa.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        
    else:
        formulario = form_comentario()
        return render(request, "hamburguesa.html",{"recetas":rec,"comentarios":com,"formulario":formulario})


def panceta(request):
    autor1 = "Paulo Airaudo"
    rec = Receta.objects.filter(autor=autor1)
    com=Comentario.objects.filter(autor=autor1)
    if request.method == "POST":
        formulario = form_comentario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            com = Comentario(Comentario = informacion["Comentario"],
            us= request.user, autor="Paulo Airaudo")
            com.save() #Guardo la data en la base de datos como en la función estudiantes.
            com=Comentario.objects.filter(autor=autor1)
            return render(request, "panceta.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        else:
            formulario = form_comentario()
            return render(request, "panceta.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        
    else:
        formulario = form_comentario()
        return render(request, "panceta.html",{"recetas":rec,"comentarios":com,"formulario":formulario})



def pechuga(request):
    autor1 = "Jorge de Andrés de Valencia."
    rec = Receta.objects.filter(autor=autor1)
    com=Comentario.objects.filter(autor=autor1)
    if request.method == "POST":
        formulario = form_comentario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            com = Comentario(Comentario = informacion["Comentario"],
            us= request.user, autor="Jorge de Andrés de Valencia.")
            com.save() #Guardo la data en la base de datos como en la función estudiantes.
            com=Comentario.objects.filter(autor=autor1)
            return render(request, "pechuga.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        else:
            formulario = form_comentario()
            return render(request, "pechuga.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        
    else:
        formulario = form_comentario()
        return render(request, "pechuga.html",{"recetas":rec,"comentarios":com,"formulario":formulario})


def steak(request):
    autor1 = "Paco López"
    rec = Receta.objects.filter(autor=autor1)
    com=Comentario.objects.filter(autor=autor1)
    if request.method == "POST":
        formulario = form_comentario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            com = Comentario(Comentario = informacion["Comentario"],
            us= request.user, autor="Paco López")
            com.save() #Guardo la data en la base de datos como en la función estudiantes.
            com=Comentario.objects.filter(autor=autor1)
            return render(request, "steak.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        else:
            formulario = form_comentario()
            return render(request, "steak.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        
    else:
        formulario = form_comentario()
        return render(request, "steak.html",{"recetas":rec,"comentarios":com,"formulario":formulario})


def taco(request):
    autor1 = "Juan Pozuelo"
    rec = Receta.objects.filter(autor=autor1)
    com=Comentario.objects.filter(autor=autor1)
    if request.method == "POST":
        formulario = form_comentario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            com = Comentario(Comentario = informacion["Comentario"],
            us= request.user, autor="Juan Pozuelo")
            com.save() #Guardo la data en la base de datos como en la función estudiantes.
            com=Comentario.objects.filter(autor=autor1)
            return render(request, "taco.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        else:
            formulario = form_comentario()
            return render(request, "taco.html",{"recetas":rec,"comentarios":com,"formulario":formulario})
        
    else:
        formulario = form_comentario()
        return render(request, "taco.html",{"recetas":rec,"comentarios":com,"formulario":formulario})


def login_request(request):
    if request.method =="POST":
        formulario = AuthenticationForm(request, data = request.POST)
        #Esta herramient necesita dos paramentros, el request, y definir el data, que 
        #debe corresponderse con el request que llene en la página. Qué información
        # viene apareada con ese POST?. Usuario y Contraseña.
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get("username")
            #username es uno de los campos del formulario, no lo vas a ver 
            #en el forms.py, es automático de django. Podría haberlo resuelto 
            #como en update_estudiante, sin el get, tendría que haber creado una 
            #instancia de un objeto usuario, y debe estar en el models.
            pwd= formulario.cleaned_data.get("password")
            user = authenticate(username= usuario, password= pwd )
            #authenticate recibe username y password. Esto inicia una sesión con los datos del 
            #formulario completo. Podría reutilizar la variable usuario
            #y pisarla con la información dle authenticate, PORQUE NO VOLVERÉ
            #A USAR usuario.
            if user is not None:#Si completaron algo, no puede venir vacío
                login(request, user)
                #Lo que hago con esta función es, si la información es válida
                #entonces genero una solicitud de loguin con los datos autenticados
                #en user.
                avatar=Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None
                return render(request, 'home.html',{'avatar':avatar})
            else:
                #Reboto la petición, porque no tipeaste nada.
                return render(request, "login.html", {"formulario":formulario})
                #Si rebota, debo enviarle el formulario para que vuelva a mostrarme
                #en loguin, el formulario para volver a completar el logueo.
        else:
            return render(request, "login.html",{"formulario":formulario})     
        #También podría disparar una pantalla de error, y con un botón volver al 
        #html que corresponde a donde estaba antes.
    else:
        formulario = AuthenticationForm()
        return render(request, "login.html",{"formulario":formulario})     
        #RECORDÁ QUE FORMULARIO ES UN FORMATO PREFABRICADO POR DJANGO
        #YA ME LO TOMA BIEN CON EL formulario.as_table EN EL HTML.
        #Así como está la función, sólo podrás salir de la web si te logueas correctamente,
        #o si cerrás el explorador, le hace falta un botón para volver al inicio.
#Al no haber creado ningun usuario en la bd, el único válido es el admin que creamos en clases anteriores.


def register(request):
    #Usaremos la herramienta de creación de usuario, ya está importada.
    formulario = FormularioDeRegistro(request.POST)#No va a haber problema porque el formulario
    #utilizado es el genérico de python, si no le pongo nada viene vacío.
    if request.method=="POST":        
        if formulario.is_valid():
            #"usuario = formulario.cleaned_data.get("username")
            formulario.save() #Puedo guardarlo en la BD porque es predefinido de Django
            #Termino guardado mi usuario y pass, ojo guarde todo el formulario, no sólo el usuario.
            avatar=Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'home.html',{'avatar':avatar}) 
            #Recordá que es el url, no el camino a la carpeta. Me lleva a la función, 
            #y de ahi a la pantalla login, ya quedo logueado.
        else:
            return render(request, "registro.html",{"formulario":formulario} )    
    formulario = FormularioDeRegistro()
    return render(request, "registro.html",{"formulario":formulario} )

@login_required()
def perfilView(request):
    avatar=Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "perfil.html",{'avatar':avatar})
#min 50:47 de django 3


@login_required
def editar_perfil(request):
    #Necesito tener una sesión iniciada, por lo tanto
    #le marco el request de inicio de sesión.
    usuario = request.user
    #La información del usuario una vez que ingrese
    #queda disponible en el navegador, y puedo obtenerla para trabajar con ella si 
    #lo necesito
    usuario_info= User.objects.get(id = usuario.id)    
    if request.method == "POST":
        formulario = UserEditForm(request.POST, instance = usuario)
        #Nuevamente creo un formulario más bello desde el form.py
        if formulario.is_valid():
            usuario_info.username = formulario.cleaned_data.get("username")
            usuario_info.email = formulario.cleaned_data.get("email")
            usuario_info.first_name =formulario.cleaned_data.get("first_name")
            usuario_info.last_name =formulario.cleaned_data.get("last_name")
            #Estos son los datos que voy a actualizar de mi formulario, estos 
            #campos son los que definimos en el form para nuestro formulario especializado,
            #La modificación debe validarse con el cleaned data, y para eso debo vincularla
            #al campo de cada input del formulario, cuyos nombres coinciden con los nombres de sus campos,
            #en este caso, username,email,firs_name y last_name. Esto se define así en la class del 
            #formulario en el forms.py.user_info tiene los mismos campos, porque son los
            # campos por defecto diseñados por django, son los campos del usuario por defecto, por eso 
            #los reconoce como campos del objeto usuario_info, y al igual que ellos diseñaré mi formulario
            #en el forms, debe coincidir.
            usuario_info.save()
            avatar=Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'home.html',{'avatar':avatar})
        else:
            avatar=Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, "home.html", {"formulario":formulario,"avatar": avatar})
            #Devolver el formulario me permite comprobar que es lo que falló.
            #Voy a tener que agregar la variable formulario en home2.html para que me indique el error.
    else:     
        formulario = UserEditForm(initial={"email":usuario.email, "username":usuario.username,
         "first_name": usuario.first_name, "last_name":usuario.last_name}) 
    return render(request, "editar_perfil.html",{"formulario":formulario,"usuario":usuario})
        #Aquí devuelvo el html de editar, formulario y usuario, ambas variables.
#Lo que hago aquí es modificar información de mi usuario, y en el caso en el que no 
#quiera modificar porque no es POST, se autocompleta con la información actual del usuario logueado, 
#lo que es condición necesaria para ejecutarse la función.


def AgregarAvatar(request):
    if request.method=="POST":
        form = AvatarFormulario(request.POST, request.FILES)
        #Cuando viene una imagen, el formulario debe recibir dos campos, la info y aparte la imagen.
        #Como debo infresar mi avatar, creo mi tipo de formulario expecífico en el forms, y obviamente
        #el método usado será "POST" desde el html.
        #EL User con mayuscula es el del modelo, OSEA LA HERRAMIENTA, y está a la par de las demás 
        # clases definidas en models, pero ya viene con django porque siempre se necesita, no neceistás crearla
        # en el models, ahora podrías partir de ella para modificarla. El user con  minúscula
        # es el usuario que está logueado, pero con el user.request, si hago una variable
        # user no es nada, es simplemente una variable. 
        if form.is_valid():
            user = User.objects.get(username= request.user)
            #Entonces ojo aca, user primero es la variable, que guarda los datos del usuario
            #respetando a la clase User, que son variables del tipo Usuario, importada en el models y 
            #aquí en el view también. Por último el que obtendré es el que coincida con el usernamda
            #que ingrese en el formulario, y para eso uso request.user, éste último user es el usuario que
            #está flotando en la web si es que alguien inicio sesión.
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id=request.user.id)
            #"avatar" es el nombre de la imagen, en la carpeta media.
            #Recordá que por más que el user tenga 2 campos, el id siempre está por detrás, es un 
            #identificado de la base de datos de ese objeto.
            #Le paso el id también, porque cuando le paso el user no le paso el id, y necesito que 
            #la imagen quede vinculada al id del perfil, por lo tanto el objeto avatar de la clase 
            #Avatar, tendrá el mismo id que el del usuario, no es el mismo dato, el usuario tiene un id
            #y la imagen otro, siempre hablando de la base de datos. Pero si quiero agregar un avatar a  usuario,
            # y lo agrego en el id de la imagen, siempre me agregará una foto nueva, yo lo que necesito es que 
            #me pise la imagen que tenía en la base de datos, para que reemplace la imagen del perfil actual.
            #De esta forma, si el id de la nueva imagen está marcado por el id del perfil, entonces al agregarse,
            #pisará la imagen con ese id, que era la imagen anterior del usuario. Cuando yo reo el objeto avatar,
            # dejo UNA SOLA IMAGEN vinculada al usuario, agregar una imagen con otro id no me sirve de nada. Necesito
            # #cambiar esa imagen de perfil pisando la anterior, asique debo conocer el id del usuario para definir el id
            # de la imagen en ese valor, y generar el reemplazo. 
            avatar.save()
            avatar=Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'home.html',{'avatar':avatar})
            #Le aclaro que me devuelva la posición 0, porque se que siempre devolverá 1, ya que
            #no puede haber dos usuarios con el mismo id. OJO CON ESTO EN MI PROYECTO, EL INDEX 0.
            #uso image.url porque nunca se guardan las imágenes en sí, sino las direcciones url. Las imágenes se 
            #guardan en servidores, con su propia base de datos, o en mi misma base de datos, pero yo invoco 
            # la url. Esta devolución tiene que ver con mostrar el avatar en home2.
    else:
        try:
            avatar=Avatar.objects.filter(user = request.user.id)
            form = AvatarFormulario() 
        except:                                                         
            form = AvatarFormulario()   
    return render(request, 'agregarAvatar.html',{'form':form})

@login_required
def changepass(request):
    usuario = request.user
    if request.method =="POST":
        form = ChangePasswordForm(data = request.POST, user = request.user)
        #Cuando se va a buscar una pass, no se busca la pass en si, sino que se busca un hash.
        #Recibe la nueva pass en el request, y necesitas el usuario en el cual querés cambiar la pass.
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            avatar=Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0],image.url
            except:
                avatar = None
            return render(request, 'home.html',{'avatar':avatar})
    else:
        form = ChangePasswordForm(user = request.user)
    return render(request, "changepass.html", {"form":form, "usuario": usuario})    




def editar_comentario_arroz(request, com_id):
    usuario_actual = request.user
    com = Comentario.objects.get(id=com_id)
    if (usuario_actual.username==com.us):
        if request.method == "POST":
            formulario = form_comentario(request.POST)#Ojo ,viene toda la carga, deben matchear, no puede faltar un campo.
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                com.Comentario = informacion["Comentario"]
                com.save()       
        formulario = form_comentario(initial={"Comentario":com.Comentario})
        return render(request, "editar_comentario.html",{"formulario":formulario,"com":com})
    
    else:
        respuesta = "Usted no está autorizado para editar este comentario."
        return HttpResponse(respuesta)

def editar_comentario_camaron(request, com_id):
    usuario_actual = request.user
    com = Comentario.objects.get(id=com_id)
    if (usuario_actual.username==com.us):
        if request.method == "POST":
            formulario = form_comentario(request.POST)#Ojo ,viene toda la carga, deben matchear, no puede faltar un campo.
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                com.Comentario = informacion["Comentario"]
                com.save()       
        formulario = form_comentario(initial={"Comentario":com.Comentario})
        return render(request, "editar_comentario_camaron.html",{"formulario":formulario,"com":com})
    
    else:
        respuesta = "Usted no está autorizado para editar este comentario."
        return HttpResponse(respuesta)


def editar_comentario_cuatroquesos(request, com_id):
    usuario_actual = request.user
    com = Comentario.objects.get(id=com_id)
    if (usuario_actual.username==com.us):
        if request.method == "POST":
            formulario = form_comentario(request.POST)#Ojo ,viene toda la carga, deben matchear, no puede faltar un campo.
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                com.Comentario = informacion["Comentario"]
                com.save()       
        formulario = form_comentario(initial={"Comentario":com.Comentario})
        return render(request, "editar_comentario_cuatroquesos.html",{"formulario":formulario,"com":com})
    
    else:
        respuesta = "Usted no está autorizado para editar este comentario."
        return HttpResponse(respuesta)


def editar_comentario_hamburguesa(request, com_id):
    usuario_actual = request.user
    com = Comentario.objects.get(id=com_id)
    if (usuario_actual.username==com.us):
        if request.method == "POST":
            formulario = form_comentario(request.POST)#Ojo ,viene toda la carga, deben matchear, no puede faltar un campo.
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                com.Comentario = informacion["Comentario"]
                com.save()       
        formulario = form_comentario(initial={"Comentario":com.Comentario})
        return render(request, "editar_comentario_hamburguesa.html",{"formulario":formulario,"com":com})
    
    else:
        respuesta = "Usted no está autorizado para editar este comentario."
        return HttpResponse(respuesta)


def editar_comentario_panceta(request, com_id):
    usuario_actual = request.user
    com = Comentario.objects.get(id=com_id)
    if (usuario_actual.username==com.us):
        if request.method == "POST":
            formulario = form_comentario(request.POST)#Ojo ,viene toda la carga, deben matchear, no puede faltar un campo.
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                com.Comentario = informacion["Comentario"]
                com.save()       
        formulario = form_comentario(initial={"Comentario":com.Comentario})
        return render(request, "editar_comentario_panceta.html",{"formulario":formulario,"com":com})
    
    else:
        respuesta = "Usted no está autorizado para editar este comentario."
        return HttpResponse(respuesta)


def editar_comentario_pechuga(request, com_id):
    usuario_actual = request.user
    com = Comentario.objects.get(id=com_id)
    if (usuario_actual.username==com.us):
        if request.method == "POST":
            formulario = form_comentario(request.POST)#Ojo ,viene toda la carga, deben matchear, no puede faltar un campo.
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                com.Comentario = informacion["Comentario"]
                com.save()       
        formulario = form_comentario(initial={"Comentario":com.Comentario})
        return render(request, "editar_comentario_pechuga.html",{"formulario":formulario,"com":com})
    
    else:
        respuesta = "Usted no está autorizado para editar este comentario."
        return HttpResponse(respuesta)


def editar_comentario_steak(request, com_id):
    usuario_actual = request.user
    com = Comentario.objects.get(id=com_id)
    if (usuario_actual.username==com.us):
        if request.method == "POST":
            formulario = form_comentario(request.POST)#Ojo ,viene toda la carga, deben matchear, no puede faltar un campo.
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                com.Comentario = informacion["Comentario"]
                com.save()       
        formulario = form_comentario(initial={"Comentario":com.Comentario})
        return render(request, "editar_comentario_steak.html",{"formulario":formulario,"com":com})
    
    else:
        respuesta = "Usted no está autorizado para editar este comentario."
        return HttpResponse(respuesta)

def editar_comentario_taco(request, com_id):
    usuario_actual = request.user
    com = Comentario.objects.get(id=com_id)
    if (usuario_actual.username==com.us):
        if request.method == "POST":
            formulario = form_comentario(request.POST)#Ojo ,viene toda la carga, deben matchear, no puede faltar un campo.
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                com.Comentario = informacion["Comentario"]
                com.save()       
        formulario = form_comentario(initial={"Comentario":com.Comentario})
        return render(request, "editar_comentario_taco.html",{"formulario":formulario,"com":com})
    
    else:
        respuesta = "Usted no está autorizado para editar este comentario."
        return HttpResponse(respuesta)

def editar_recetas_amateur(request, r_id):
    usuario_actual = request.user
    rec1 = Receta_Amateur.objects.get(id=r_id)
    if (usuario_actual.username==rec1.us):
        if request.method == "POST":
            formulario = form_receta(request.POST)#Ojo ,viene toda la carga, deben matchear, no puede faltar un campo.
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                rec1.nombre=informacion["nombre"]
                rec1.ingrediente=informacion['ingrediente']
                rec1.autor=informacion['autor']
                rec1.texto=informacion['texto']
                rec1.save()
                rec = Receta_Amateur.objects.all()          
        formulario = form_receta(initial={"nombre":rec1.nombre,
        "ingrediente":rec1.ingrediente,"autor":rec1.autor,"texto":rec1.texto,"fecha":rec1.fecha})
        return render(request, "editar_tus_recetas.html",{"formulario":formulario,"id":r_id})  
    else:
        respuesta = "Usted no está autorizado para editar esta receta."
        return HttpResponse(respuesta)



def eliminar_comentario(request,com_id ):#Debe entrar el dato que quiero eliminar.
    usuario_actual = request.user
    com = Comentario.objects.get(id=com_id)
    if (usuario_actual.username==com.us):
    #Traigo a estu, un objeto de la BD que coincida con el parámetro ingresado.
    #El modo directo sería tipear el mail directamente, pero tengo que usar el nombre
    #del atributo del modelo estudiante, es el método por nombre.
        com.delete()
        formulario = form_comentario()
        return render(request, "eliminar_comentario.html")
    else:
        respuesta = "No está autorizado para eliminar este comentario"
        return HttpResponse(respuesta)

def eliminar_tus_recetas(request,id ):#Debe entrar el dato que quiero eliminar.
    usuario_actual = request.user
    rec1 = Receta_Amateur.objects.get(id=id)
    if (usuario_actual.username==rec1.us):
    #Traigo a estu, un objeto de la BD que coincida con el parámetro ingresado.
    #El modo directo sería tipear el mail directamente, pero tengo que usar el nombre
    #del atributo del modelo estudiante, es el método por nombre.
        rec1.delete()
        rec = Receta_Amateur.objects.all()
        return render(request, "eliminar_tus_recetas.html")
    else:
        respuesta = "No está autorizado para eliminar esta receta."
        return HttpResponse(respuesta)


@login_required
def tus_recetas(request):
    rec = Receta_Amateur.objects.all()  
    return render(request, "tus_recetas.html",{"recetas":rec})       


def agregar_receta(request):
        if request.method == "POST":
            formulario = form_receta(request.POST)#Ojo ,viene toda la carga, deben matchear, no puede faltar un campo.
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                rec = Receta_Amateur(nombre = informacion["nombre"],
                ingrediente= informacion['ingrediente'], autor=informacion['autor'], 
                texto=informacion['texto'],us=request.user)
                rec.save()       
        formulario = form_receta()
        return render(request, "agregar_receta.html",{"formulario":formulario})
    
