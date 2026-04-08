from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticia, Comentario

def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'lista.html', {'noticias': noticias})


def detalhe_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'noticia.html', {'noticia': noticia})


def comentarios(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    comentarios = Comentario.objects.filter(noticia=noticia)

    if request.method == 'POST':
        texto = request.POST.get('texto')
        Comentario.objects.create(noticia=noticia, texto=texto)
        return redirect('comentarios', id=noticia.id)

    return render(request, 'comentarios.html', {
        'noticia': noticia,
        'comentarios': comentarios
    })
