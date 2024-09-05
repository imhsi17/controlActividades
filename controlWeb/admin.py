from django.contrib import admin
from controlWeb.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class Empresa_resource(resources.ModelResource):
    
    class Meta:
        model = Empresa

class Estado_resource(resources.ModelResource):
    
    class Meta:
        model = Estado

class Actividad_resource(resources.ModelResource):
    
    class Meta:
        model = Actividad

class Tarea_resource(resources.ModelResource):
    
    class Meta:
        model = Tarea

class Jornada_resource(resources.ModelResource):
    
    class Meta:
        model = Jornada

class Empresa_admin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ("nombre_empresa", "id", "ruc", "rubro", "correo_empresa")
    list_filter = ("rubro",)
    resource_class = Empresa_resource

class Estado_admin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ("nombre", "id")
    resource_class = Estado_resource

class Actividad_admin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ("nombre_actividad", "id","tiempo_establecido_actividad", "estado_actividad")
    search_fields = ("nombre_actividad",)
    list_filter = ("estado_actividad",)
    resource_class = Actividad_resource

class Tarea_admin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ("nombre_tarea", "id","descripcion_tarea", "tiempo_establecido_tarea")
    search_fields = ("nombre_tarea",)
    list_filter = ("estado_tarea",)
    resource_class = Tarea_resource

class Jornada_admin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ("tarea","comentario", "hora_inicio", "hora_final", "tiempo_empleado", "trabajador")
    search_fields = ("fecha_realizada",)
    list_filter = ("trabajador",)
    resource_class = Jornada_resource

# Register your models here.

admin.site.register(Empresa, Empresa_admin)
admin.site.register(Estado, Estado_admin)
admin.site.register(Actividad, Actividad_admin)
admin.site.register(Tarea, Tarea_admin)
admin.site.register(Jornada, Jornada_admin)

