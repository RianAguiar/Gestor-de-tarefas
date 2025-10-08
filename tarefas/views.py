from django.shortcuts import render

def tarefas(request):
    return render(request,'home/index.html')