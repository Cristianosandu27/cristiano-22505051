from django import forms
from .models import Curso, Professor, Aluno


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'