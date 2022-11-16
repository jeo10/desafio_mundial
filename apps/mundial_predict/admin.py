from django.contrib import admin
from apps.mundial_predict.models import *


class SeleccionAdmin(admin.ModelAdmin):
    list_display = ('codigo_seleccion', 'nombre')


class PartidoAdmin(admin.ModelAdmin):
    list_display = ('codigo_partido',)


admin.site.register(Seleccion, SeleccionAdmin)
admin.site.register(Partido, PartidoAdmin)
