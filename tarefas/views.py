from django.shortcuts import render , redirect, get_object_or_404
from .models import tarefaModels
from .forms import tarefaForm
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

'''-------------------------------------------------------------------------------------------------'''

def tarefas_index(request):
    return render(request, 'tarefas/index.html')

'''-------------------------------------------------------------------------------------------------'''

def tarefas_cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmar = request.POST['confirmar']
        if senha != confirmar:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('tarefas:cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
            return redirect('tarefas:cadastro')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.success(request, 'Conta criada com sucesso! Faça login.')
        return redirect('tarefas:login')
    return render(request, 'tarefas/cadastro.html')

'''-------------------------------------------------------------------------------------------------'''

def tarefas_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=senha)
            if user is not None:
                login(request, user)
                return redirect('tarefas:home')
            else:
                messages.error(request, 'Email ou senha inválidos.')
        except User.DoesNotExist:
            messages.error(request, 'Usuário não encontrado.')
    return render(request, 'tarefas/login.html')

'''-------------------------------------------------------------------------------------------------'''

def logout_view(request):
    logout(request)
    return redirect('tarefas:login')

'''-------------------------------------------------------------------------------------------------'''

@login_required(login_url='tarefas:login')
def tarefas_home(request):
    context={
        'tarefas':tarefaModels.objects.all()
    }
    return render(request,'tarefas/home.html',context)

'''-------------------------------------------------------------------------------------------------'''

@login_required(login_url='tarefas:login')
def tarefas_adicionar(request:HttpRequest):
    if request.method == 'POST':
        formulario = tarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')
    context={'form' : tarefaForm } 
    return render(request,'tarefas/adicionar.html', context)

'''-------------------------------------------------------------------------------------------------'''

@login_required(login_url='tarefas:login')
def tarefas_remover(request:HttpRequest,id):
    item = get_object_or_404(tarefaModels, id=id)
    item.delete()
    return redirect('tarefas:home')

'''-------------------------------------------------------------------------------------------------'''

@login_required(login_url='tarefas:login')
def tarefas_editar(request:HttpRequest,id):
    item = get_object_or_404(tarefaModels, id=id)
    if request.method == 'POST':
        formulario = tarefaForm(request.POST, instance=item)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')
    formulario = tarefaForm(instance=item)
    context={'form' : formulario }
    return render(request,'tarefas/editar.html', context)