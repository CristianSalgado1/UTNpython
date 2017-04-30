from django.contrib import admin
from vistaprevia.models import Productos
# Register your models here.

class PreguntasAdmin(admin.ModelAdmin):
    fields  = ['fecha_publicacion',  'producto']

admin.site.register(Productos,  PreguntasAdmin)

