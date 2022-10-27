from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm



class FormularioDeRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese su Password", widget = forms.PasswordInput())
    password2 = forms.CharField(label="Ingrese Nuevamente su contraseña", widget = forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields} #Quitar los mensajes de ayuda
        #Envía el mensaje "", es decir vacío, por cada k en fields.


class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    avatar = forms.ImageField()
    #No hereda de nadie, por lo tanto no tiene mayor dificultad.
    #No te confundas, este no es le modelo, eso está en models, esta es la edición de 
    #como se verá el formulario para agregar el avatar, y sólo requiere la imagen.


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="", widget= forms.PasswordInput(attrs={'placeholder': "Old Password"}))
    new_password1 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "New password"}))
    new_password2 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "Confirm new password"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}
    

class form_comentario(forms.Form):
    Comentario = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Comentario'}))
    #Aquí tomo la info del models estudiantes, la idea es 
    #al igual que el modelo, y los input´s que defino en el html, pueda
    # definir un formulario directamente como en los models, ahorrandome
    #la codificaciones de los input.
    class Meta:
        model = User
        fields = ['Comentario']
        help_texts = {k:"" for k in fields}

class form_receta(forms.Form):
    nombre = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Tu Receta'}))
    ingrediente = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Ingredientes'}))
    texto = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Elaboración'}))
    autor = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Tu nombre'}))
    #Aquí tomo la info del models estudiantes, la idea es 
    #al igual que el modelo, y los input´s que defino en el html, pueda
    # definir un formulario directamente como en los models, ahorrandome
    #la codificaciones de los input.
    class Meta:
        model = User
        fields = ['nombre','ingrediente','texto','autor']
        help_texts = {k:"" for k in fields}
    