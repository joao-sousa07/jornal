from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_noticias, name='lista'),
    path('noticia/<int:id>/', views.detalhe_noticia, name='noticia'),
    path('noticia/<int:id>/comentarios/', views.comentarios, name='comentarios'),
]