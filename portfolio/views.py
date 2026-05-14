from django.shortcuts import render

from .models import (
    Licenciatura,
    Docente,
    Categoria,
    Tecnologia,
    Competencia,
    Formacao,
    TFC,
    Projeto,
    UnidadeCurricular,
    MakingOf,
)


def portfolio_view(request):
    context = {
        "licenciaturas": Licenciatura.objects.all(),
        "docentes": Docente.objects.all(),
        "categorias": Categoria.objects.all(),
        "tecnologias": Tecnologia.objects.all(),
        "competencias": Competencia.objects.all(),
        "formacoes": Formacao.objects.all(),
        "tfcs": TFC.objects.all(),
        "projetos": Projeto.objects.all(),
        "unidades": UnidadeCurricular.objects.all(),
        "makingofs": MakingOf.objects.all(),
    }

    return render(request, "portfolio/portfolio.html", context)