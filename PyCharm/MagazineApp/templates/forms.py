# import formularza kreacji
from django.contrib.auth.forms import UserCreationForm

# import modeli formularzy
from django import forms

# import modeli użytkownika
from django.contrib.auth.models import User

# edycja formularza kreacji żeby był własny tekst
class ForDodPrac(UserCreationForm):
    class Meta:
        model = User
        # https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/#overriding-the-default-fields
        fields = ['username', 'email', 'password1', 'password2', 'groups']
        labels = {
            'username': 'Nazwa Użytkownika :',
            'email': 'Email służbowy :',
        }
        password1 = forms.CharField(label="Podaj hasło :")
        password2 = forms.CharField(label="Potwierdź hasło :")
