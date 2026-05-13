from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos_view, name='cursos'),

    path('curso/criar/', views.curso_criar, name='curso_criar'),
    path('curso/<int:id>/editar/', views.curso_editar, name='curso_editar'),
    path('curso/<int:id>/apagar/', views.curso_apagar, name='curso_apagar'),

    path('professores/', views.professores_view, name='professores'),
    path('professor/criar/', views.professor_criar, name='professor_criar'),
    path('professor/<int:id>/editar/', views.professor_editar, name='professor_editar'),
    path('professor/<int:id>/apagar/', views.professor_apagar, name='professor_apagar'),

    path('alunos/', views.alunos_view, name='alunos'),
    path('aluno/criar/', views.aluno_criar, name='aluno_criar'),
    path('aluno/<int:id>/editar/', views.aluno_editar, name='aluno_editar'),
    path('aluno/<int:id>/apagar/', views.aluno_apagar, name='aluno_apagar'),
]