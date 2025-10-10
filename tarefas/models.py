from django.db import models

class tarefaModels(models.Model):
    status = models.BooleanField(default=False)
    nome = models.CharField(max_length=67)
    descricao = models.CharField(null=True, blank=True, max_length=69)
    dataDeCricao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome
    