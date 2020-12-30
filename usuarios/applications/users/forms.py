from django import forms
from django.contrib.auth import authenticate
 
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(label = 'contraseña',required=True,widget=forms.PasswordInput(
        attrs= {
            'placeholder':'Contraseña'
            }
        )
    )

    password2 = forms.CharField(label = 'contraseña',required=True,widget=forms.PasswordInput(
        attrs= {
            'placeholder':'Repetir contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
            
            )
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2','Las contraseñas no son iguales')
        lista=self.cleaned_data['password1']
        if  len(lista)<= 5:
            self.add_error('password1','Ingrese una contraseña mayor a 5 digitos!')


#creo mi formulario a libertad porque no quiero
#trabajar directamente con el modelo
class LoginForm(forms.Form):
    username = forms.CharField(label = 'contraseña',required=True,widget=forms.TextInput(
        attrs= {
            'placeholder':'username',
            'style':'{margin:10px}',
            }
        )
    )
    password = forms.CharField(label = 'contraseña',required=True,widget=forms.PasswordInput(
        attrs= {
            'placeholder':'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username,password=password):
            raise forms.ValidationError("Los datos son incorrectos")

        return self.cleaned_data
        
        
class UpdateForm(forms.Form):
    password1 = forms.CharField(label = 'contraseña',required=True,widget=forms.PasswordInput(
        attrs= {
            'placeholder':'Contraseña'
            }
        )
    )

    password2 = forms.CharField(label = 'contraseña',required=True,widget=forms.PasswordInput(
        attrs= {
            'placeholder':'Nueva contraseña'
            }
        )
    )

class VerificacionForm(forms.Form):
    codregistro = forms.CharField(required=True)

    

