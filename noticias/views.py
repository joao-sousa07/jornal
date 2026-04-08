from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticia, Comentario
from .forms import ComentarioForm

def lista_noticias(request):
    noticias = Noticia.objects.all()
    # Agora aponta para a subpasta noticias/
    return render(request, 'noticias/lista.html', {'noticias': noticias})

def detalhe_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    comentarios = noticia.comentarios.all()
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.noticia = noticia
            comentario.save()
            return redirect('detalhe_noticia', id=noticia.id)
    else:
        form = ComentarioForm()
    
    # Agora aponta para a subpasta noticias/
    return render(request, 'noticias/noticia.html', {
        'noticia': noticia,
        'comentarios': comentarios,
        'form': form
    })