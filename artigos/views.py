from django.contrib.auth.decorators import (
    login_required,
    user_passes_test
)

from django.shortcuts import (
    render,
    redirect
)

from .models import Artigo
from .forms import ArtigoForm


def autor(user):
    return user.groups.filter(
        name='autores'
    ).exists()


def artigos_view(request):

    artigos = Artigo.objects.all().order_by(
        '-data_criacao'
    )

    context = {
        'artigos': artigos
    }

    return render(
        request,
        'artigos/artigos.html',
        context
    )


@login_required
@user_passes_test(autor)
def artigo_criar(request):

    if request.method == 'POST':

        form = ArtigoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            artigo = form.save(commit=False)

            artigo.autor = request.user

            artigo.save()

            return redirect('artigos')

    else:

        form = ArtigoForm()

    return render(
        request,
        'artigos/artigo_form.html',
        {'form': form}
    )