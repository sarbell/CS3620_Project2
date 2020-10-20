from django.contrib import admin
from .models import BrickElement,SeptemberElement, Lib, RockElement


# Register your models here.

admin.site.register(BrickElement)
admin.site.register(SeptemberElement)
admin.site.register(RockElement)
admin.site.register(Lib)