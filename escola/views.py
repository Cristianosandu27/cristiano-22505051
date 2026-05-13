from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

from .models import Curso, Professor, Aluno
from .forms import CursoForm, ProfessorForm, AlunoForm


def gestor(user):
    return user.groups.filter(name='gestor_portfolio').exists()


# =========================
# CURSOS
# =========================

def cursos_view(request):
    context = {
        'cursos': Curso.objects.all()
    }

    return render(request, 'escola/cursos.html', context)


@login_required
@user_passes_test(gestor)
def curso_criar(request):

    if request.method == 'POST':
        form = CursoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cursos')

    else:
        form = CursoForm()

    return render(request, 'escola/curso_form.html', {'form': form})


@login_required
@user_passes_test(gestor)
def curso_editar(request, id):

    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)

        if form.is_valid():
            form.save()
            return redirect('cursos')

    else:
        form = CursoForm(instance=curso)

    return render(request, 'escola/curso_form.html', {'form': form})


@login_required
@user_passes_test(gestor)
def curso_apagar(request, id):

    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':
        curso.delete()
        return redirect('cursos')

    return render(request, 'escola/curso_apagar.html', {'curso': curso})


# =========================
# PROFESSORES
# =========================

def professores_view(request):

    context = {
        'professores': Professor.objects.all()
    }

    return render(request, 'escola/professores.html', context)


@login_required
@user_passes_test(gestor)
def professor_criar(request):

    if request.method == 'POST':
        form = ProfessorForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('professores')

    else:
        form = ProfessorForm()

    return render(request, 'escola/professor_form.html', {'form': form})


@login_required
@user_passes_test(gestor)
def professor_editar(request, id):

    professor = get_object_or_404(Professor, id=id)

    if request.method == 'POST':
        form = ProfessorForm(request.POST, request.FILES, instance=professor)

        if form.is_valid():
            form.save()
            return redirect('professores')

    else:
        form = ProfessorForm(instance=professor)

    return render(request, 'escola/professor_form.html', {'form': form})


@login_required
@user_passes_test(gestor)
def professor_apagar(request, id):

    professor = get_object_or_404(Professor, id=id)

    if request.method == 'POST':
        professor.delete()
        return redirect('professores')

    return render(request, 'escola/professor_apagar.html', {'professor': professor})


# =========================
# ALUNOS
# =========================

def alunos_view(request):

    context = {
        'alunos': Aluno.objects.all()
    }

    return render(request, 'escola/alunos.html', context)


@login_required
@user_passes_test(gestor)
def aluno_criar(request):

    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('alunos')

    else:
        form = AlunoForm()

    return render(request, 'escola/aluno_form.html', {'form': form})


@login_required
@user_passes_test(gestor)
def aluno_editar(request, id):

    aluno = get_object_or_404(Aluno, id=id)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)

        if form.is_valid():
            form.save()
            return redirect('alunos')

    else:
        form = AlunoForm(instance=aluno)

    return render(request, 'escola/aluno_form.html', {'form': form})


@login_required
@user_passes_test(gestor)
def aluno_apagar(request, id):

    aluno = get_object_or_404(Aluno, id=id)

    if request.method == 'POST':
        aluno.delete()
        return redirect('alunos')

    return render(request, 'escola/aluno_apagar.html', {'aluno': aluno})