from django import forms 
from .models import tarefaModels


class tarefaForm(forms.ModelForm):
    class Meta:
        model = tarefaModels
        fields = ['status','nome','descricao']
