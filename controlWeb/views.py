from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.http import Http404
from django.contrib import messages
from controlWeb.models import *
from datetime import datetime
import locale

# Create your views here.

def login_usuario(request):
    
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Credenciales Incorrectas!")
        
    return render(request, "login.html")

def inicio(request):
    
    datos = {}
    empresas = Empresa.objects.all()
    
    if empresas:
        for empresa in empresas:
            id_empresa = empresa.id
            actividades = Actividad.objects.filter(empresa=id_empresa)
            datos[str(empresa.nombre_empresa)] = actividades
    context = {"empresas":empresas, "datos":datos}

    return render(request, "index.html", context)

def tareas(request, id):
    
    try:
        tareas = Tarea.objects.filter(actividad=id).order_by('id')
        actividad = Actividad.objects.get(id=id)
    
        context = {"tareas":tareas, "actividad":actividad}
    
        return render(request, "tareas.html", context)
    
    except Actividad.DoesNotExist:
        
        return render(request, "error.html", {"mensaje":"Sin tareas que listar!!"})

def nueva_incidencia(request, id):
    
    try:
        #locale.setlocale(locale.LC_TIME, 'es_PE.UTF-8')
        hora = datetime.now().time().strftime("%H:%M")
        fecha = datetime.now().date().strftime("%Y-%m-%d")
        tarea = Tarea.objects.get(id=id)
        if request.method == "POST":
            
            fecha_tarea = request.POST.get('fecha_realizada')
            hora_inicio = request.POST.get('hora_inicio')
            hora_fin = request.POST.get('hora_fin')
            comentario = request.POST.get('comentario')
            progreso = request.POST.get('progreso')
            tiempo_empleado = datetime.strptime(request.POST.get('hora_fin'),"%H:%M") - datetime.strptime(request.POST.get('hora_inicio'),"%H:%M")
            trabajador = request.user
            tarea_incidencia = tarea
            
            incidencia = Jornada(fecha_realizada=fecha_tarea, hora_inicio=hora_inicio, hora_final=hora_fin,
                                 comentario=comentario, progreso=progreso, tiempo_empleado=str(tiempo_empleado),
                                 trabajador=trabajador, tarea=tarea_incidencia)
            
            incidencia.save()
            messages.success(request, "Incidencia Guardada con Éxito!")
            
            return redirect('/')

        context = {"tarea":tarea, "hora":hora, "fecha":fecha}
        return render(request, "incidencia_nueva.html", context)
    
    except Tarea.DoesNotExist:
        
        return render(request, "error.html", {"mensaje":"La tarea no existe!!"})

def incidencias(request):
    
    #locale.setlocale(locale.LC_TIME, 'es_PE.UTF-8')
    fecha = datetime.now().date().strftime("%Y-%m-%d")
    incidencias = Jornada.objects.filter(fecha_realizada=fecha)
    
    context = {"fecha":fecha, "incidencias":incidencias}    
    return render(request, "incidencias.html", context)

def salir(request):
    
    logout(request)
    return redirect("/login")


