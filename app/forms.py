"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import grunddaten

class BootstrapAuthenticationForm(AuthenticationForm):

    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'i': 'form-control',
                                   'placeholder':'Password'}))

    sapname = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'id': 'sapname',
                                   'placeholder': 'Sap'}))
    vorname = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'id': 'vorname',
                                   'placeholder':'vorname'}))

class grunddaten(forms.ModelForm):
    sapname= forms.CharField(widget=forms.Textarea)
    vorname= forms.CharField(widget=forms.Textarea)
    nachname = forms.CharField(widget=forms.Textarea)
    instno = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'size':'10'}))
    einrichtung = forms.CharField(widget=forms.Textarea)
    email = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(widget=forms.Textarea)
    finanzstelle = forms.CharField(widget=forms.Textarea)
    GültigVon = forms.CharField(widget=forms.Textarea)
    GültigBis = forms.CharField(widget=forms.Textarea)