from django.contrib import admin
from .models import (
    Licenciatura,
    UnidadeCurricular,
    Docente,
    Projeto,
    TFC,
    Tecnologia,
    Categoria,
    Competencia,
    Formacao,
    MakingOf,
    FotoMakingOf,
)


class FotoMakingOfInline(admin.TabularInline):
    model = FotoMakingOf
    extra = 1


class MakingOfAdmin(admin.ModelAdmin):
    inlines = [FotoMakingOfInline]


admin.site.register(Licenciatura)
admin.site.register(UnidadeCurricular)
admin.site.register(Docente)
admin.site.register(Projeto)
admin.site.register(TFC)
admin.site.register(Tecnologia)
admin.site.register(Categoria)
admin.site.register(Competencia)
admin.site.register(Formacao)
admin.site.register(MakingOf, MakingOfAdmin)
admin.site.register(FotoMakingOf)