from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import (
    urlsafe_base64_encode,
    urlsafe_base64_decode
)
from django.utils.encoding import (
    force_bytes,
    force_str
)

from .forms import RegistoForm
from .tokens import magic_link_token


def registo_view(request):

    if request.method == "POST":

        form = RegistoForm(request.POST)

        if form.is_valid():

            user = form.save()

            grupo = Group.objects.get(name="autores")
            user.groups.add(grupo)

            return redirect("login")

    else:
        form = RegistoForm()

    return render(
        request,
        "accounts/registo.html",
        {"form": form}
    )


def login_view(request):

    erro = ""

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("cursos")

        else:
            erro = "Nome de utilizador ou palavra-passe inválidos."

    return render(
        request,
        "accounts/login.html",
        {"erro": erro}
    )


def logout_view(request):

    logout(request)

    return redirect("login")


def magic_link_request(request):

    mensagem = ""

    if request.method == "POST":

        email = request.POST.get("email")

        user = User.objects.filter(email=email).first()

        if user:

            uid = urlsafe_base64_encode(
                force_bytes(user.pk)
            )

            token = magic_link_token.make_token(user)

            link = request.build_absolute_uri(
                reverse(
                    "magic_link_login",
                    kwargs={
                        "uidb64": uid,
                        "token": token
                    }
                )
            )

            print("LINK MÁGICO:", link)

        mensagem = (
            "Se existir uma conta com esse email, "
            "foi enviado um link mágico."
        )

    return render(
        request,
        "accounts/magic_link.html",
        {"mensagem": mensagem}
    )


def magic_link_login(request, uidb64, token):

    try:

        uid = force_str(
            urlsafe_base64_decode(uidb64)
        )

        user = User.objects.get(pk=uid)

    except Exception:

        user = None

    if (
        user is not None
        and magic_link_token.check_token(user, token)
    ):

        login(request, user)

        return redirect("cursos")

    return render(
        request,
        "accounts/magic_link_invalido.html"
    )