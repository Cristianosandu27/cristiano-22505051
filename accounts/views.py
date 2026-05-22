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

from django.core.mail import send_mail
from django.conf import settings

from .forms import RegisterForm
from .tokens import magic_link_token


def registo_view(request):

    if request.user.is_authenticated:
        return redirect("cursos")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            grupo, created = Group.objects.get_or_create(
                name="gestor-portfolio"
            )

            user.groups.add(grupo)

            return redirect("login")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/registo.html",
        {"form": form}
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect("cursos")

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

            base_url = "https://super-meme-974ppw6w6wjpcpw56-8000.app.github.dev"

            link = base_url + reverse(
                "magic_link_login",
                kwargs={
                    "uidb64": uid,
                    "token": token
                }
            )

            send_mail(
                "O teu link mágico",
                f"Clica neste link para entrar: {link}",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

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