from django.http import FileResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as dj_login, logout as dj_logout, authenticate
from django.contrib import messages
from .models import Page, Precio
from django.db import connection



# Create your views here.
def sesion(request):
    return render(request,'mainapp/sesion.html')

def create(request):
    if request.method =="POST":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM auth_user ")
            datos = cursor.fetchall()
        dato = len(datos)
        if dato >= 2:
            messages.error(request,"Has Superado El Limite De Registros")
            return render(request,'mainapp/sesion.html')
        else:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                usuario = form.save()
                nombre_usuario = form.cleaned_data.get('username')
                messages.success(request, f"Nueva Cuenta Creada: {nombre_usuario} " )
                dj_login(request,usuario)
                return redirect('index')
            else:
                for msg in form.error_messages:
                    messages.error(request," Ha Ocurrido Un Error")
                
    form = UserCreationForm
    return render(request,'mainapp/crear_user.html', {"form":form})

def login(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password=contraseña)
            
            if user is not None:
                dj_login(request, user)
                messages.success(request, f"Estas Logeado Como {usuario} ")
                return redirect('index')
            else:
                messages.error(request, "Usuario O Contraseña No Valido")       
        else:
            messages.error(request, "Usuario O Contraseña No Valido")
            
    form = AuthenticationForm()
    return render(request, "mainapp/login.html", {"form": form})

def logout(request):
    dj_logout(request)
    messages.info(request, "Saliste Exitosamente")
    return redirect('sesion')

def index(request):
    return render(request,'mainapp/index.html')

def consulta(request):
    return render(request,'mainapp/consulta.html')

def seccion_consulta(request):
    
    return render(request,'mainapp/seccion_consulta.html')

def crear_casa(request):
    if request.method == 'POST':
        from datetime import datetime
        now = datetime.today().strftime('%d-%m-%Y')
        
        
        proyecto = request.POST.get('proyecto')
        poligono = request.POST.get('poligono')
        casa = request.POST.get('casa')
        modelo = request.POST.get('modelo')
        contratista = request.POST.get('contratista')
        codigoobra = request.POST.get('codigoobra')
        porcentaje = request.POST.get('porcentaje')
        agrupacion = request.POST.get('agrupacion')
        username = request.user.username

        
        
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT precio_agru24 FROM main_precio WHERE modelo_casa = %s", [modelo])
            row = cursor.fetchone()
            num = row[0]
            
        with connection.cursor() as cursor:
            cursor.execute("SELECT precio_agru25 FROM main_precio WHERE modelo_casa = %s", [modelo])
            row1 = cursor.fetchone()
            num1 = row1[0]
            
        with connection.cursor() as cursor:
            cursor.execute("SELECT precio_agru26 FROM main_precio WHERE modelo_casa = %s", [modelo])
            row2 = cursor.fetchone()
            num2 = row2[0]
            
        if agrupacion == 'AGRUPACION No°24':
            if porcentaje == '0':
                agru_precio = 0
                casa_new = Page(
                    proyecto_casa = proyecto,
                    modelo_casa = modelo,
                    poligono_casa = poligono,
                    numero_casa = casa,
                    contratista_casa = contratista,
                    estado_contratista = True,
                    obra_casa = codigoobra,
                    agrupacion_casa = agrupacion,
                    precio_agru = agru_precio,
                    porcentaje_casa = porcentaje,
                    content = "No Hay Comentarios",
                    progreso_casa = 1,
                    fecha_generica = now,
                    creado_user = username,
                    update_user = "No Hay Actualizaciones"
                    
                )
                messages.success(request, f"Has Agregado Una Casa Exitosamente")
                casa_new.save()
                
            elif porcentaje == '0.5':
                division =  num / 2
                agru_precio = division
                casa_new = Page(
                    proyecto_casa = proyecto,
                    modelo_casa = modelo,
                    poligono_casa = poligono,
                    numero_casa = casa,
                    contratista_casa = contratista,
                    estado_contratista = True,
                    obra_casa = codigoobra,
                    agrupacion_casa = agrupacion,
                    precio_agru = agru_precio,
                    porcentaje_casa = porcentaje,
                    content = "No hay Comentarios",
                    progreso_casa = 1,
                    fecha_generica = now,
                    creado_user = username,
                    update_user = "No Hay Actualizaciones"
                )
                messages.success(request, f"Has Agregado Una Casa Exitosamente")
                casa_new.save()
            elif porcentaje == '1.0':
                agru_precio = num
                casa_new = Page(
                    proyecto_casa = proyecto,
                    modelo_casa = modelo,
                    poligono_casa = poligono,
                    numero_casa = casa,
                    contratista_casa = contratista,
                    estado_contratista = True,
                    obra_casa = codigoobra,
                    agrupacion_casa = agrupacion,
                    precio_agru = agru_precio,
                    porcentaje_casa = porcentaje,
                    content = "No Hay Comentarios",
                    progreso_casa = 1,
                    fecha_generica = now,
                    creado_user = username,
                    update_user = "No Hay Actualizaciones"
                )
                messages.success(request, f"Has Agregado Una Casa Exitosamente")
                casa_new.save()
        elif agrupacion == 'AGRUPACION No°25':
                if porcentaje == '0':
                    agru_precio = 0
                    casa_new = Page(
                        proyecto_casa = proyecto,
                        modelo_casa = modelo,
                        poligono_casa = poligono,
                        numero_casa = casa,
                        contratista_casa = contratista,
                        estado_contratista = True,
                        obra_casa = codigoobra,
                        agrupacion_casa = agrupacion,
                        precio_agru = agru_precio,
                        porcentaje_casa = porcentaje,
                        content = "No Hay Comentarios",
                        progreso_casa = 1,
                        fecha_generica = now,
                        creado_user = username,
                        update_user = "No Hay Actualizaciones"
                    )
                    messages.success(request, f"Has Agregado Una Casa Exitosamente")
                    casa_new.save()
                    
                elif porcentaje == '0.5':
                    division =  num1 / 2
                    agru_precio = division
                    casa_new = Page(
                        proyecto_casa = proyecto,
                        modelo_casa = modelo,
                        poligono_casa = poligono,
                        numero_casa = casa,
                        contratista_casa = contratista,
                        estado_contratista = True,
                        obra_casa = codigoobra,
                        agrupacion_casa = agrupacion,
                        precio_agru = agru_precio,
                        porcentaje_casa = porcentaje,
                        content = "No Hay Comentarios",
                        progreso_casa = 1,
                        fecha_generica = now,
                        creado_user = username,
                        update_user = "No Hay Actualizaciones"
                    )
                    messages.success(request, f"Has Agregado Una Casa Exitosamente")
                    casa_new.save()
                elif porcentaje == '1.0':
                    agru_precio = num1
                    casa_new = Page(
                        proyecto_casa = proyecto,
                        modelo_casa = modelo,
                        poligono_casa = poligono,
                        numero_casa = casa,
                        contratista_casa = contratista,
                        estado_contratista = True,
                        obra_casa = codigoobra,
                        agrupacion_casa = agrupacion,
                        precio_agru = agru_precio,
                        porcentaje_casa = porcentaje,
                        content = "No Hay Comentarios",
                        progreso_casa = 1,
                        fecha_generica = now,
                        creado_user = username,
                        update_user = "No Hay Actualizaciones"
                    )
                    messages.success(request, f"Has Agregado Una Casa Exitosamente")
                    casa_new.save()
        elif agrupacion == 'AGRUPACION No°26':
                if porcentaje == '0':
                    agru_precio = 0
                    casa_new = Page(
                        proyecto_casa = proyecto,
                        modelo_casa = modelo,
                        poligono_casa = poligono,
                        numero_casa = casa,
                        contratista_casa = contratista,
                        estado_contratista = True,
                        obra_casa = codigoobra,
                        agrupacion_casa = agrupacion,
                        precio_agru = agru_precio,
                        porcentaje_casa = porcentaje,
                        content = "No Hay Comentarios",
                        progreso_casa = 1,
                        fecha_generica = now,
                        creado_user = username,
                        update_user = "No Hay Actualizaciones"
                    )
                    messages.success(request, f"Has Agregado Una Casa Exitosamente")
                    casa_new.save()
                    
                elif porcentaje == '0.5':
                    division =  num2 / 2
                    agru_precio = division
                    casa_new = Page(
                        proyecto_casa = proyecto,
                        modelo_casa = modelo,
                        poligono_casa = poligono,
                        numero_casa = casa,
                        contratista_casa = contratista,
                        estado_contratista = True,
                        obra_casa = codigoobra,
                        agrupacion_casa = agrupacion,
                        precio_agru = agru_precio,
                        porcentaje_casa = porcentaje,
                        content = "No Hay Comentarios",
                        progreso_casa = 1,
                        fecha_generica = now,
                        creado_user = username,
                        update_user = "No Hay Actualizaciones"
                    )
                    messages.success(request, f"Has Agregado Una Casa Exitosamente")
                    casa_new.save()
                elif porcentaje == '1.0':
                    agru_precio = num2
                    casa_new = Page(
                        proyecto_casa = proyecto,
                        modelo_casa = modelo,
                        poligono_casa = poligono,
                        numero_casa = casa,
                        contratista_casa = contratista,
                        estado_contratista = True,
                        obra_casa = codigoobra,
                        agrupacion_casa = agrupacion,
                        precio_agru = agru_precio,
                        porcentaje_casa = porcentaje,
                        content = "No Hay Comentarios",
                        progreso_casa = 1,
                        fecha_generica = now,
                        creado_user = username,
                        update_user = "No Hay Actualizaciones"
                    )
                    messages.success(request, f"Has Agregado Una Casa Exitosamente")
                    casa_new.save()
                

    return render(request,'mainapp/crear_casa.html')

def busquedaA(request):
    if request.method == 'POST':
        global proyecto_search
        global poligono_search
        global casa_search
        global modelo_search
        global contratista_search
        global codigoobra_search
        proyecto_search = request.POST.get('proyecto')
        poligono_search = request.POST.get('poligono')
        casa_search  = request.POST.get('casa')
        modelo_search  = request.POST.get('modelo')
        contratista_search  = request.POST.get('contratista')
        codigoobra_search  = request.POST.get('codigoobra')
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM main_page WHERE  poligono_casa = %s AND numero_casa = %s AND modelo_casa= %s AND contratista_casa= %s AND obra_casa = %s AND proyecto_casa = %s",[poligono_search ,casa_search ,modelo_search ,contratista_search ,codigoobra_search,proyecto_search ])
            global_casa = cursor.fetchall()
        return render(request,'mainapp/consultaA.html',{'global_casa': global_casa})
    
    return render(request,'mainapp/busquedaA.html')

def busquedaB(request):
    
    if request.method == 'POST':
        proyecto = request.POST.get('proyecto')
        poligono= request.POST.get('poligono')
        casa = request.POST.get('casa')
        modelo  = request.POST.get('modelo')
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM main_page WHERE poligono_casa = %s AND numero_casa = %s AND modelo_casa= %s AND proyecto_casa = %s",[poligono,casa,modelo,proyecto])
            global_casa = cursor.fetchall()
        return render(request,'mainapp/consultaB.html',{'global_casa': global_casa})
    return render(request,'mainapp/busquedaB.html')
  
def busquedaC(request):
    proyecto = request.POST.get('proyecto')
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM main_page WHERE proyecto_casa = %s ORDER BY id DESC",[proyecto])
            info_casa = cursor.fetchall()
        return render(request,'mainapp/consulta.html',{'info_casa': info_casa})
    return render(request,'mainapp/busquedaC.html')
    
def consultaA(request):
    return render(request,'mainapp/consultaA.html')

def consultaB(request):
    return render(request,'mainapp/consultaB.html')

def modificar(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT precio_agru24 FROM main_precio WHERE modelo_casa = %s", [modelo_search])
        row = cursor.fetchone()
        num = row[0]
            
    with connection.cursor() as cursor:
        cursor.execute("SELECT precio_agru25 FROM main_precio WHERE modelo_casa = %s", [modelo_search])
        row1 = cursor.fetchone()
        num1 = row1[0]
        
    with connection.cursor() as cursor:
        cursor.execute("SELECT precio_agru26 FROM main_precio WHERE modelo_casa = %s", [modelo_search])
        row2 = cursor.fetchone()
        num2 = row2[0]
            
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM main_page WHERE poligono_casa = %s AND numero_casa = %s AND modelo_casa= %s AND contratista_casa= %s AND obra_casa = %s",[poligono_search ,casa_search ,modelo_search ,contratista_search ,codigoobra_search])
        global_casa = cursor.fetchall()
        
        for casa_var in global_casa:
            idcasa = casa_var[0]
            
    if request.method == 'POST':
        porcentaje = request.POST.get('porcentaje')
        agrupacion = request.POST.get('agrupacion')
        progreso = request.POST.get('progreso')
        update_casa = Page.objects.get(pk=idcasa)
        username = request.user.username
        update_casa.update_user = username

        if agrupacion == 'AGRUPACION No°24':
            if porcentaje == '0':
                agru_precio = 0
                update_casa.porcentaje_casa = porcentaje
                update_casa.precio_agru= agru_precio
                update_casa.agrupacion_casa = agrupacion
                update_casa.progreso_casa = progreso
                
                update_casa.save()
                messages.success(request, f"Has Modificado Una Casa Exitosamente")
                return render(request,'mainapp/modificar.html')
            
            elif porcentaje == '0.5':
                division =  num / 2
                agru_precio = division
                update_casa.porcentaje_casa = porcentaje
                update_casa.precio_agru= agru_precio
                update_casa.agrupacion_casa = agrupacion
                update_casa.progreso_casa = progreso
                
                update_casa.save()
                messages.success(request, f"Has Modificado Una Casa Exitosamente")
                return render(request,'mainapp/modificar.html')
                
            elif porcentaje == '1.0':
                agru_precio = num
                update_casa.porcentaje_casa = porcentaje
                update_casa.precio_agru = agru_precio
                update_casa.agrupacion_casa = agrupacion
                update_casa.progreso_casa = progreso
                
                update_casa.save()
                messages.success(request, f"Has Modificado Una Casa Exitosamente")
                return render(request,'mainapp/modificar.html')
        elif agrupacion == 'AGRUPACION No°25':
            if porcentaje == '0':
                agru_precio = 0
                update_casa.porcentaje_casa = porcentaje
                update_casa.precio_agru = agru_precio
                update_casa.agrupacion_casa = agrupacion
                update_casa.progreso_casa = progreso
                
                update_casa.save()
                messages.success(request, f"Has Modificado Una Casa Exitosamente")
                return render(request,'mainapp/modificar.html')
            
            elif porcentaje == '0.5':
                division =  num1 / 2
                agru_precio = division
                update_casa.porcentaje_casa = porcentaje
                update_casa.precio_agru = agru_precio
                update_casa.agrupacion_casa = agrupacion
                update_casa.progreso_casa = progreso
                
                update_casa.save()
                messages.success(request, f"Has Modificado Una Casa Exitosamente")
                return render(request,'mainapp/modificar.html')
                
            elif porcentaje == '1.0':
                agru_precio = num1
                update_casa.porcentaje_casa = porcentaje
                update_casa.precio_agru = agru_precio
                update_casa.agrupacion_casa = agrupacion
                update_casa.progreso_casa = progreso
                
                update_casa.save()
                messages.success(request, f"Has Modificado Una Casa Exitosamente")
                return render(request,'mainapp/modificar.html')
        elif agrupacion == 'AGRUPACION No°26':
                if porcentaje == '0':
                    agru_precio = 0
                    update_casa.porcentaje_casa = porcentaje
                    update_casa.precio_agru = agru_precio
                    update_casa.agrupacion_casa = agrupacion
                    update_casa.progreso_casa = progreso
                    
                    update_casa.save()
                    messages.success(request, f"Has Modificado Una Casa Exitosamente")
                    return render(request,'mainapp/modificar.html')
                
                elif porcentaje == '0.5':
                    division =  num2 / 2
                    agru_precio = division
                    update_casa.porcentaje_casa = porcentaje
                    update_casa.precio_agru = agru_precio
                    update_casa.agrupacion_casa = agrupacion
                    update_casa.progreso_casa = progreso
                    
                    update_casa.save()
                    messages.success(request, f"Has Modificado Una Casa Exitosamente")
                    return render(request,'mainapp/modificar.html')
                    
                elif porcentaje == '1.0':
                    agru_precio = num2
                    update_casa.porcentaje_casa = porcentaje
                    update_casa.precio_agru = agru_precio
                    update_casa.agrupacion_casa = agrupacion
                    update_casa.progreso_casa = progreso
                    
                    update_casa.save()
                    messages.success(request, f"Has Modificado Una Casa Exitosamente")
                    return render(request,'mainapp/modificar.html')
                    
# TODO Futuro Aqui Se Agregaran nuevos Modelos de Casa Solo Cambiando El Nombre 'example'                 

    return render(request,'mainapp/modificar.html')

def chat(request):
    return render(request,'mainapp/lobby_chat.html')
        
def modificar_pdf(request):
    if request.method == 'POST':
        inmo = request.POST.get('inmo')
        orden = request.POST.get('orden')
        residente = request.POST.get('residente')
        cancelada = request.POST.get('cancelada')
        año = request.POST.get('año')
        planilla = request.POST.get('planilla')
        retencion = request.POST.get('retencion')
        empleado = request.POST.get('empleado')
        dui = request.POST.get('dui')
        proyecto = request.POST.get('proyecto')
        fecha_inicio = request.POST.get('fecha1')
        fecha_final = request.POST.get('fecha2')
        subir = request.POST.get('subir')

        import xlsxwriter
        import random
        from datetime import datetime

        #* Conexion A La DB 
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM main_page WHERE proyecto_casa = '{proyecto}' AND created_at BETWEEN '{fecha_inicio}' AND '{fecha_final}' ")
            datos = cursor.fetchall()
            

        # Fecha actual
        now = datetime.today().strftime('%d-%m-%Y')
        nowday = datetime.today().strftime('%H:%M:%S')
        today = datetime.today().strftime('%d-%m-%Y %H-%M-%S')
        


        #? Nombre Del Documento
        workbook = xlsxwriter.Workbook('Control.xlsx')
        worksheet = workbook.add_worksheet()
        #? Orientacion De La Pagina
        worksheet.set_landscape()
        worksheet.protect('Construm@s0000')

        # Negrita
        bold = workbook.add_format({'bold': True})
        # Tamaño De Letra
        font_size = workbook.add_format()
        font_size.set_font_size(8)
        # Alineacion
        font_size.set_align('left')




        worksheet.write('A1', inmo.upper(),font_size)
        worksheet.write('A2', 'ORDEN DE TRABAJO, PAGO POR OBRA',font_size)
        
        worksheet.write('A4', 'N° DE ORDEN: ' + orden ,font_size)
        worksheet.write('A5', proyecto.upper() ,font_size)
        worksheet.write('A6', 'ESTADO: CREADO',font_size)
        worksheet.write('A7', 'LISTADO DEL: '+ fecha_inicio + '    AL: '+ fecha_final ,font_size)
        
        
        
        
        worksheet.write('A9', 'EMPLEADO: '+ empleado.upper(),font_size)
        worksheet.write('A10', 'DUI: '+ dui,font_size)
        worksheet.write('C9', 'CONSTRUMAS S.A DE C.V ',font_size)
        
        
        worksheet.write('G5', 'RESIDENTE:  '+ residente.upper() ,font_size)
        worksheet.write('G6', 'OBRA CANCELADA: ' + cancelada,font_size)
        worksheet.write('G7', 'RETENCION CANCELADA: '+ retencion,font_size)
        
        worksheet.write('J6', 'PLANILLA N°: '+ planilla,font_size)
        worksheet.write('L6', 'AÑO: '+ año,font_size)
        

        worksheet.write('K1', 'FECHA:',font_size)
        worksheet.write('L1', now ,font_size)
        worksheet.write('K2', 'HORA:',font_size)
        worksheet.write('L2', nowday ,font_size)
        worksheet.write('K3', 'DIGITO:',font_size)





        #? el primer parametro es la fila , el segundo es el texto 
        worksheet.write('A12', 'MODELO ',font_size)
        worksheet.write('B12', 'POLIGONO',font_size)
        worksheet.write('C12', 'NUM CASA',font_size)
        worksheet.write('D12', 'OBRA',font_size)
        worksheet.write('E12', 'CONTRATISTA',font_size)
        worksheet.write('H12', 'AGRUPACION',font_size)
        worksheet.write('J12', 'PRECIO',font_size)
        worksheet.write('K12', 'PORCENTAJE',font_size)
        worksheet.write('L12', 'SUB TOTAL ',font_size)





        nombre = [item[1] for item in datos]
        worksheet.write_column(13, 0, nombre,font_size)

        poligono = [item[2] for item in datos]
        worksheet.write_column(13, 1, poligono,font_size)

        numcasa = [item[3] for item in datos]
        worksheet.write_column(13, 2, numcasa,font_size)

        obra = [item[4] for item in datos]
        worksheet.write_column(13, 3, obra,font_size)

        contratista = [item[9] for item in datos]
        worksheet.write_column(13, 4, contratista,font_size)

        agrupacion = [item[5] for item in datos]
        worksheet.write_column(13, 7, agrupacion,font_size)

        precio = [item[12] for item in datos]
        worksheet.write_column(13, 9, precio,font_size)
        worksheet.write_column(13, 11, precio,font_size)

        porcentaje = [item[6] for item in datos]
        worksheet.write_column(13, 10,porcentaje,font_size)



        total = precio
        resultado = sum(total)

        #* Separacion Del Total 
        info_extra = 15
        info = len(datos)
        suma = info + info_extra

        worksheet.write(suma,8, 'TOTAL:', font_size)
        worksheet.write(suma,9, "$ "+str(resultado), font_size)



        workbook.close()


        #* Convertir a PDF
        import win32com
        from win32com import client
        import os
        import pythoncom
        #currentDir = os.path.abspath('.')
        currentDir = os.getcwd()
        xlApp = win32com.client.Dispatch("Excel.Application",pythoncom.CoInitialize())
        books = xlApp.Workbooks.Open(os.path.join(currentDir,"Control.xlsx"))    
        ws = books.Worksheets[0]
        ws.Visible = 1
        
        
        
        if subir == 'on':
            ruta = 'C:\\Users\\vegar\\Documents\\Proyecto\\Doc'
            ws.ExportAsFixedFormat(0,os.path.join(ruta, today))
            ws.ExportAsFixedFormat(0,os.path.join(currentDir,"Control" ) )
            books.Close()
            print("XLSX to PDF conversion sucessful and Saved")
        elif subir == None:
            ws.ExportAsFixedFormat(0,os.path.join(currentDir,"Control" ) )
            books.Close()
            print("XLSX to PDF conversion sucessful and Saved")


        return FileResponse(open('Control.pdf', 'rb'), content_type='application/pdf')
        
    return render(request,'mainapp/modificar_pdf.html')


def error_404(request, exception):
    return render(request, 'mainapp/404.html')