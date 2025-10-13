from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.tarefas, name='home'),
    path('adicionar/', views.tarefas_adicionar, name='adicionar'),
    path('editar/<int:id>/', views.tarefas_editar, name='editar'),
    path('remover/<int:id>/', views.tarefas_remover, name='remover'),


]
