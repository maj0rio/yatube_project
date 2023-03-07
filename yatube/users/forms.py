from django import forms
from django.contrib.auth import password_validation
from django.forms import TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Пароль',
                                          'autocomplete': 'new-password'
                                          }),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Подтверждение пароля',
                                          'autocomplete': 'new-password'
                                          }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

        widgets = {
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                _("The two password fields didn't match."),
                code='password_mismatch',
            )

        return cleaned_data


class CustomUserChangeForm(UserChangeForm):

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Пароль',
                                          'autocomplete': 'new-password'
                                          }),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'Подтверждение пароля',
                                          'autocomplete': 'new-password'
                                          }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

        widgets = {
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                _("The two password fields didn't match."),
                code='password_mismatch',
            )

        return cleaned_data
