from django import forms
from .models import Lib


class LibForm(forms.Form):
    field = 'hi'

