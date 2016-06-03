# coding: utf-8

from django import forms
from django.forms import TextInput
from th_ellie.models import Ellie


class EllieForm(forms.ModelForm):

    """
        for to handle Pocket service
    """

    class Meta:
        model = Ellie
        fields = ('name',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class EllieProviderForm(EllieForm):
    pass


class EllieConsumerForm(EllieForm):
    pass
