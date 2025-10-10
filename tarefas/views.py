from django.shortcuts import render
from .forms import tarefaForm

def tarefas(request):
    return render(request,'index.html')



def tarefas_adicionar(request):
    contexto={
    'form':tarefaForm  
    } 
    return render(request,'adicionar.html')
