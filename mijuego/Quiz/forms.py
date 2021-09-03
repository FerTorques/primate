from django import forms
from django.core.exceptions import ValidationError
from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model

User=get_user_model()

class ElegirInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super(ElegirInlineFormSet, self).clean()

        respuesta_correcta=0
        for formulario in self.forms:
            if not formulario.is_valid():
                return
            
            if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
                respuesta_correcta +=1
            
        try:
            assert respuesta_correcta == Pregunta.NUMERO_DE_RESPUESTAS_PERMITIDAS
        except AssertionError:
            raise forms.ValidationError('Solo puede elegir una respuesta como correcta')


class UsuarioLoginFormulario(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if username and password:
            user=authenticate(username=username, password=password)
            if not user:
                raise ValidationError('El usuario NO existe')
            if not user.check_password(password):
                raise ValidationError('Contraseña incorrecta')
            if not user.is_active:
                raise ValidationError('Este usuario no esta activo')
            return super(UsuarioLoginFormulario, self).clean(*args, **kwargs)

class RegistroFormulario(UserCreationForm):
    nick = forms.CharField(required=True, max_length=20)
    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields = [
            'nick',
            'email',
            'username'
        ]

