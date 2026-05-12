from django.shortcuts import render
from .models import Curso


def cursos_view(request):

    context = {
        'cursos': Curso.objects.all()
    }

    return render(request, 'escola/cursos.html', context)