from django.contrib import admin
from app11.models import *

class InscripcionInline(admin.TabularInline):
    model = Inscripcion
    extra = 1
    verbose_name = "Inscripcion"
    verbose_name = "Inscripciones"

class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'departamento', 'instructor')    
    list_filter = ('departamento', 'instructor')
    search_fields = ('titulo',)
    inlines = (InscripcionInline,)

class EntregasInline(admin.TabularInline):
    model = Entrega
    extra = 1
    verbose_name = "Entrega"
    verbose_name = "Entregas"

class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_entrega', 'curso')    
    list_filter = ('fecha_entrega', 'curso')
    search_fields = ('titulo',)
    inlines = (EntregasInline,)

admin.site.register(Departamento)
admin.site.register(Instructor)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Entrega)
