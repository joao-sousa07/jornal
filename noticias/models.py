from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)

    def __str__(self):
        return self.titulo

# Create your models here.
