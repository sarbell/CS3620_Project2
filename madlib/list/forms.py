from django import forms
from .models import BrickElement, SeptemberElement, RockElement, CookieElement


class BrickForm(forms.ModelForm):
    class Meta:
        model = BrickElement
        fields = [
            "field1",
            "field2",
            "field3",
            "field4",
            "field5",
            "field6",
            "field7",
            "field8",
            "field9",
        ]


class SeptemberForm(forms.ModelForm):
    class Meta:
        model = SeptemberElement
        fields = [
            "field1",
            "field2",
            "field3",
            "field4",
            "field5",
            "field6",
            "field7",
            "field8",
            "field9",
            "field10",
            "field11",
            "field12",
            "field13",
            "field14",
            "field15",
            "field16",
        ]

class RockForm(forms.ModelForm):
    class Meta:
        model = RockElement
        fields = [
            "field1",
            "field2",
            "field3",
            "field4",
            "field5",
            "field6",
            "field7",
            "field8",
        ]

class CookieForm(forms.ModelForm):
    class Meta:
        model = CookieElement
        fields = [
            "field1",
            "field2",
            "field3",
            "field4",
            "field5",
            "field6",
            "field7",
            "field8",
            "field9",
            "field10",
            "field11",
            "field12",
            "field13",
        ]
