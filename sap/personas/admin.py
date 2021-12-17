
from django.contrib import admin

# Register your models here.
from personas.models import Persona
admin.site.register(Persona)

from personas.models import Domicilio
admin.site.register(Domicilio)