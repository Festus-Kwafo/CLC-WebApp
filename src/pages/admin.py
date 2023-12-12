from django.contrib import admin

# Register your models here.

from .models import Event, Message

admin.site.register(Event)