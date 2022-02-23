from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm, fields, widgets
from .models import User

input_class = "input-field"

class UserChangeForms(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
   
        
class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    
        
class RegisterForm(ModelForm):
    
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'gender',
            'bio',
            'password',
        )
        
        widgets = {
            'first_name': widgets.TextInput(
                attrs={
                    'placeholder': "Seu primeiro nome",
                    'class': input_class,
                    'required': True,
                }
            ),
            'last_name': widgets.TextInput(
                attrs={
                    'placeholder': "Seu último nome",
                    'class': input_class,
                }
            ),
            'username': widgets.TextInput(
                attrs={
                    'placeholder': "Seu nicknmae",
                    'class': input_class,
                    'required': True,
                }
            ),
            'email': widgets.EmailInput(
                attrs={
                    'placeholder': 'your_email@adrss.com',
                    'class': input_class,
                    'required': True,
                }
            ),
            'bio': widgets.TextInput(
                attrs={
                    'placeholder': 'Escreva sobre você(opcional)',
                    'class': input_class,
                }
            ),
            'gender': widgets.Select(
                attrs={
                    'placeholder': 'Seu Gênero',
                    'class': input_class,
                    'required': True,
                }
            ),
            'password': widgets.PasswordInput(
                attrs={
                    'placeholder': 'Digite a sua senha',
                    'class': input_class,
                    'required': True,
                }
            ),
        }
        
    
class LoginForm(ModelForm):
    
    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )
        widgets = {
            'username': widgets.TextInput(
                attrs={
                    'placeholder': "Seu nickname",
                    'class': input_class,
                    'id': 'login_username',
                    'required': True,
                }      
            ),
            'password': widgets.PasswordInput(
                attrs={
                    'placeholder': 'Digite a sua senha',
                    'class': input_class,
                    'id': 'login_password',
                    'required': True,
                }
            ),
        }