from django.shortcuts import render
from django.http import HttpResponse

def tarefas(request):
    return render(request,'home/index.html')

def tarefas_adicionar(request):
    return HttpResponse('adicionar')
