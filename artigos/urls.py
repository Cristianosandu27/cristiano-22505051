from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.artigos_view,
        name='artigos'
    ),

    path(
        'criar/',
        views.artigo_criar,
        name='artigo_criar'
    ),
]