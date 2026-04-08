from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'texto']
        widgets = {
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome'
            }),
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escreva seu comentário...'
            })
        }
        labels = {
            'autor': 'Nome',
            'texto': 'Comentário'
        }