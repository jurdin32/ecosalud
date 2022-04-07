from django.contrib import admin

# Register your models here.
from Prestadores.models import Departamentos, Municipios, SedesPrestador, DetalleSede
from ecosalud.snippers import Attr

admin.site.site_header = "EGESS"
admin.site.site_title = "Portal Administrativo"
admin.site.index_title = "Bienvenidos al portal Ecosistema de Gestion de Servicios Seguros"



class MunicipiosInline(admin.StackedInline):
    model = Municipios
    extra = 0

@admin.register(Departamentos)
class modelo(admin.ModelAdmin):
    list_display = Attr(Departamentos)
    list_display_links = Attr(Departamentos)
    inlines = [MunicipiosInline]

@admin.register(Municipios)
class modelo(admin.ModelAdmin):
    list_display = Attr(Municipios)
    list_display_links = Attr(Municipios)

class SedesInline(admin.StackedInline):
    model = DetalleSede
    extra = 0

@admin.register(SedesPrestador)
class modelo(admin.ModelAdmin):
    list_display = Attr(SedesPrestador)
    list_display_links = Attr(SedesPrestador)
    inlines = [SedesInline]
    search_fields = ['nombre_prestador']


@admin.register(DetalleSede)
class modelo(admin.ModelAdmin):
    list_display = Attr(DetalleSede)
    list_display_links = Attr(DetalleSede)
    search_fields = ['nombre']