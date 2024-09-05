from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Empresa(models.Model):
    
    id = models.AutoField(primary_key=True, blank=False, null=False)
    nombre_empresa = models.CharField('Nombre', blank=False, null=False, max_length=150)
    ruc = models.CharField('RUC', max_length=11, blank=False, null=False)
    direccion = models.CharField('Dirección', blank=False, null=False, max_length=250)
    correo_empresa = models.CharField('Correo', blank=False, null=False, max_length=150)
    rubro = models.CharField('Rubro', blank=True, null=False, max_length=150)
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self):
        return self.nombre_empresa

class Estado(models.Model):
    
    id = models.AutoField(primary_key=True, blank=False, null=False)
    nombre = models.CharField('Nombre', blank=False, null=False, max_length=75)
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
    
    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    
    id = models.AutoField(primary_key=True, blank=False, null=False)
    nombre_actividad = models.CharField('Actividad', blank=False, null=False, max_length=150)
    tiempo_establecido_actividad = models.IntegerField('Tiempo Establecido', blank=False, null=False)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    estado_actividad = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
    
    def __str__(self):
        return self.nombre_actividad

class Tarea(models.Model):
    
    id = models.AutoField(primary_key=True, blank=False, null=False)
    nombre_tarea = models.CharField('Nombre', blank=False, null=False, max_length=150)
    descripcion_tarea = models.TextField('Descripción', blank=False, null=False)
    tiempo_establecido_tarea = models.IntegerField('Tiempo Establecido', blank=False, null=False)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    estado_tarea = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
    
    def __str__(self):
        return self.nombre_tarea

class Jornada(models.Model):
    
    id = models.AutoField(primary_key=True, blank=False, null=False)
    fecha_realizada = models.DateField('Fecha Realizada')
    hora_inicio = models.TimeField('Hora Inicio', blank=False, null=False)
    hora_final = models.TimeField('Hora Fin', blank=False, null=False)
    comentario = models.TextField('Comentario', blank=False, null=False)
    progreso = models.IntegerField('Progreso', blank=False, null=False)
    tiempo_empleado = models.TimeField('Tiempo Empleado', blank=False, null=False)
    trabajador = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Jornada'
        verbose_name_plural = 'Jornadas'
    
    def __str__(self) -> str:
        return f"{self.tarea}: {self.trabajador}, {self.tiempo_empleado}-{self.progreso}"


