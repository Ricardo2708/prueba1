from django.contrib import admin
from .models import Page, Precio,Contratista,Proyectos,Inmobiliaria,Anuncio
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('agrupacion_casa', 'precio_agru', 'fecha_generica','porcentaje_casa','obra_casa','creado_user','created_at','update_user','updated_at',)
    
class AdAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at')

admin.site.register(Page, PageAdmin)
admin.site.register(Precio, AdAdmin)
admin.site.register(Contratista,AdAdmin)
admin.site.register(Proyectos, AdAdmin)
admin.site.register(Inmobiliaria, AdAdmin)
admin.site.register(Anuncio, AdAdmin)

#Configuracion Del Panel
title = "Panel De Administracion (Construmas)"
subtitle = "Control De Proyectos"

admin.site.site_header =  title
admin.site.site_title = title
admin.site.index_title = subtitle

