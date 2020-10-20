from django import forms
from .models import BrickElement, SeptemberElement, RockElement,\
    CookieElement, SoupElement, RageElement, QuoteElement, Poem1Element, Poem3Element, StoryElement


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


class SoupForm(forms.ModelForm):
    class Meta:
        model = SoupElement
        fields = [
            "field1",
            "field2",
            "field3",
            "field4",
            "field5",
            "field6",
            "field7",
            "field8",
            "field9"
        ]

class RageForm(forms.ModelForm):
    class Meta:
        model = RageElement
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
        ]


class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteElement
        fields = [
            "field1",
            "field2",
            "field3",
            "field4",
            "field5",
            "field6",
            "field7",
        ]


class Poem1Form(forms.ModelForm):
    class Meta:
        model = Poem1Element
        fields = [
            "field1",
            "field2",
            "field3",
            "field4",
        ]


class Poem3Form(forms.ModelForm):
    class Meta:
        model = Poem3Element
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
        ]

class StoryForm(forms.ModelForm):
    class Meta:
        model = StoryElement
        fields = [
            "field1",
            "field2",
            "field3",
            "field4",
            "field5",
            "field6",
            "field7",
        ]