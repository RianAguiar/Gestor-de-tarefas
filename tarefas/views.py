from django.shortcuts import render , redirect, get_object_or_404
from .models import tarefaModels
from .forms import tarefaForm
from django.http import HttpRequest

def tarefas_index(request):
    return render(request,'index.html')

def tarefas_login(request):
    return render(request,'login.html')

def tarefas_cadastro(request):
    return render(request,'cadastro.html')

def tarefas_home(request):
    context={
        'tarefas':tarefaModels.objects.all()
    }
    return render(request,'home.html',context)


def tarefas_adicionar(request:HttpRequest):
    if request.method == 'POST':
        formulario = tarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')
    context={'form' : tarefaForm } 
    return render(request,'adicionar.html', context)

def tarefas_remover(request:HttpRequest,id):
    item = get_object_or_404(tarefaModels, id=id)
    item.delete()
    return redirect('tarefas:home')

def tarefas_editar(request:HttpRequest,id):
    item = get_object_or_404(tarefaModels, id=id)
    if request.method == 'POST':
        formulario = tarefaForm(request.POST, instance=item)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')
    formulario = tarefaForm(instance=item)
    context={'form' : formulario }
    return render(request,'editar.html', context)