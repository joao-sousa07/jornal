from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)  # título -> titulo
    conteudo = models.TextField()  # conteúdo -> conteudo
    data = models.DateTimeField(auto_now_add=True)  # data_publicacao -> data
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comentário de {self.autor}'
    
    class Meta:
        ordering = ['-data_criacao']
