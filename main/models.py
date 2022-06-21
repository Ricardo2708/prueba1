from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Page(models.Model):
    proyecto_casa = models.CharField(max_length=50, verbose_name="Proyecto Al Que Pertenece")
    modelo_casa = models.CharField(max_length=50, verbose_name="Modelo De Casa")
    poligono_casa = models.CharField(max_length=50, verbose_name="Poligono De Casa")
    numero_casa = models.IntegerField(verbose_name="Numero De Casa")
    contratista_casa = models.CharField(max_length=50, verbose_name="Contratista De La Casa")
    estado_contratista = models.BooleanField(verbose_name="Estado Del Contratista")
    obra_casa = models.CharField(max_length=50, verbose_name="Codigo De Obra")
    agrupacion_casa = models.CharField(max_length=100,verbose_name="Agrupacion")
    precio_agru = models.FloatField(verbose_name="Precio De La Agrupacion $ ")
    porcentaje_casa = models.FloatField(verbose_name="Porcentaje %")
    content = models.TextField(verbose_name="Comentarios", blank=True)
    progreso_casa = models.IntegerField(verbose_name="Progreso De La Casa")
    fecha_generica = models.CharField(max_length=50, verbose_name="Fecha Generica")
    creado_user = models.CharField(max_length=50, verbose_name="Creado Por ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Creacion El')
    update_user = models.CharField(max_length=50, verbose_name="Actualizado Por")
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Fecha De Actualizacion')
    
    class Meta:
        verbose_name = "Casa"
        verbose_name_plural = "Casas"
        
    def __str__(self):
        return self.modelo_casa
    
    
    
class Precio(models.Model):
    modelo_casa = models.CharField(unique = True, max_length=50, verbose_name="Modelo De Casa")
    precio_agru24 = models.FloatField(verbose_name="Precio De La Agrupacion 24")
    precio_agru25 = models.FloatField(verbose_name="Precio De La Agrupacion 25")
    precio_agru26 = models.FloatField(verbose_name="Precio De La Agrupacion 26")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El ')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El ')
    
    class Meta:
        verbose_name = "Precio De Agrupacion"
        verbose_name_plural = "Precios De Agrupaciones"
        
    def __str__(self):
        return self.modelo_casa
    
class Contratista(models.Model):
    nombre_persona = models.CharField(unique = True, max_length=50, verbose_name="Nombre")
    dui_persona = models.CharField(unique = True, max_length=50, verbose_name="Dui")
    nit_persona = models.CharField(unique = True, max_length=50, verbose_name="Nit")
    estado_contratista = models.BooleanField(verbose_name="Estado Del Contratista")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El ')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El ')
    
    class Meta:
        verbose_name = "Contratista"
        verbose_name_plural = "Contratistas"
        
    def __str__(self):
        return self.nombre_persona
    
class Proyectos(models.Model):
    nombre_proyecto = models.CharField(unique = True, max_length=50, verbose_name="Nombre Del Proyecto")
    lugar_proyecto = models.CharField(unique = True, max_length=50, verbose_name="Lugar Del Proyecto")
    estado_proyecto = models.BooleanField(verbose_name="Estado Del Proyecto")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El ')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El ')
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        
    def __str__(self):
        return self.nombre_proyecto

class Inmobiliaria(models.Model):
    nombre_inmo = models.CharField(unique = True, max_length=50, verbose_name="Nombre de La Inmobiliaria")
    pertenecia_inmo = models.CharField(unique = True, max_length=50, verbose_name="Proyecto Al Que Pertenece")
    estado_proyecto = models.BooleanField(verbose_name="Estado Del Proyecto")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El ')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El ')
    
    class Meta:
        verbose_name = "Inmobiliaria"
        verbose_name_plural = "Inmobiliaria"
        
    def __str__(self):
        return self.nombre_inmo
            
            
            
class Anuncio(models.Model):
    name_anuncio = models.CharField(max_length=50, verbose_name="Nombre De Quien Anuncia")
    title_anuncio = models.CharField(unique = True, max_length=50, verbose_name="Titulo Del Anuncio")
    content_anuncio = RichTextField(verbose_name="Mensaje", blank=True)
    state_anuncio = models.BooleanField(verbose_name="¿Visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El ')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El ')
    
    class Meta:
        verbose_name = "Anuncio"
        verbose_name_plural = "Anuncios"
        
    def __str__(self):
        return self.title_anuncio