from main.models import Page,Contratista,Proyectos,Inmobiliaria,Precio,Anuncio

def get_pages(request):
    pages = Page.objects.values_list('id','modelo_casa','poligono_casa','numero_casa','contratista_casa','estado_contratista','obra_casa','agrupacion_casa','porcentaje_casa','content','created_at','updated_at','progreso_casa','precio_agru','proyecto_casa','creado_user','update_user')
    return {
        'pages': pages
    }
    
def get_contratista(request):
    contratista = Contratista.objects.values_list('id','nombre_persona','estado_contratista')
    return {
        'contratista': contratista
    }
    
def get_proyectos(request):
    proyectos = Proyectos.objects.values_list('id','nombre_proyecto','estado_proyecto')
    return{
        'proyectos': proyectos
    }
    
def get_inmo(request):
    inmobiliaria = Inmobiliaria.objects.values_list('id','nombre_inmo')
    return{
        'inmobiliaria': inmobiliaria
    }
    
def get_precio(request):
    casa_precio = Precio.objects.values_list('modelo_casa')
    return{
        'casa_precio': casa_precio
    }

def get_anuncio(request):
    anuncio = Anuncio.objects.filter(state_anuncio=True).values_list('name_anuncio','title_anuncio','content_anuncio')
    return{
        'anuncio': anuncio
    }