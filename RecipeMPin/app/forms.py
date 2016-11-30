"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))
    # pin = forms.IntegerField(widget=forms.PasswordInput({
    #     'class': 'form-control',
    #     'placeholder': 'Pin'}))


class Loginpin(forms.Form):
    pin = forms.IntegerField(label=_("Pin"),
                             widget=forms.PasswordInput({
                                 'class': 'form-control',
                                 'placeholder': 'PIN'}))


# class Register(forms.Form):
#     username = forms.CharField(max_length=254,
#                                widget=forms.TextInput({
#                                    'class': 'form-control',
#                                    'placeholder': 'User name'}))
#     password = forms.IntegerField(label=_("Password"),
#                                   widget=forms.PasswordInput({
#                                       'class': 'form-control',
#                                       'placeholder': 'PIN'}))
