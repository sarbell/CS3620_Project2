from django.contrib import admin
from .models import BrickElement,SeptemberElement, Lib, \
RockElement, SoupElement, RageElement, QuoteElement,Poem1Element, Poem3Element,  StoryElement


# Register your models here.

admin.site.register(BrickElement)
admin.site.register(SeptemberElement)
admin.site.register(RockElement)
admin.site.register(SoupElement)
admin.site.register(RageElement)
admin.site.register(QuoteElement)
admin.site.register(Poem1Element)
admin.site.register(Poem3Element)
admin.site.register(StoryElement)

admin.site.register(Lib)