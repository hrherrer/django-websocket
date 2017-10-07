from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label=u'Nombre de usuario')
    password1 = forms.CharField(widget=forms.PasswordInput, label=u'Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label=u'Confirmar contraseña')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        help_texts = {
            'password2': 'asd',
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True, label=u'Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput, label=u'Contraseña')


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True, label=u'Nombre')
    last_name = forms.CharField(max_length=30, required=True, label=u'Apellidos')
    email = forms.EmailField(max_length=50, required=True, label=u'Correo electrónico')
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
