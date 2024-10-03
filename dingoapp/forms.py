from django import forms

from blogapp.models import User
from dingoapp.models import BookingModel


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name *',

            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            'num_of_g': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of guests *',
                'type': 'number'
            }),
            'date': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date * (yyyy-mm-dd)',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number *',
            }),
            'time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Time * (hh:mm)',
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'Textarea',
                'placeholder': 'Your Note',
                'rows': "4"
            })

        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'single-input',
                'placeholder': 'Username',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'single-input',
                'placeholder': 'Password',
            })
        }
