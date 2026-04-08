from django.shortcuts import render
from .models import Noticia

def lista_noticias(request):
    noticias = Noticia.objects.all().order_by('-data_publicacao')
    return render(request, 'noticias/lista.html', {'noticias': noticias})

# Create your views here.
