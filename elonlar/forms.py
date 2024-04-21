from django import forms
from .models import Avtomobillar, Category, Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class AvtoForm(forms.ModelForm):
    class Meta:
        model = Avtomobillar
        fields = ['name', 'content', 'category', 'photo', 'views', 'published']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Avtomobil nomi',
                'style': 'margin-top: 10px'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Avtomobilhaqida',
                'style': 'margin-top: 10px'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Kategoriya',
                'style': 'margin-top: 10px'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rasm',
                'style': 'margin-top: 10px'
            }),
            'views': forms.NumberInput(attrs={
                'class': 'form-control-sm',
                'placeholder': 'Ko\'rishlar soni',
                'style': 'margin-top: 10px'
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'margin-top: 10px',
                'placeholder': 'Ko\'rishlar'
            })
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Kategoriya',
                'style': 'margin-top: 10px'
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'style': 'margin-top: 10px'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'style': 'margin-top: 10px'
    }))


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 
        'class': 'form-control',
        'placeholder': 'Repeat the password'
    }))

    class Meta:
        model = User
        fields = ('username', 'email')





class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']


