from django.db import models
from django.contrib.auth.models import User

class tarefaModels(models.Model):
    status = models.BooleanField(default=False)
    nome = models.CharField(max_length=67)  
    descricao = models.TextField(null=True, blank=True )
    dataDeCricao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome