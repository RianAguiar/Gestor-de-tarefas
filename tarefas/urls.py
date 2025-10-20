from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.tarefas_index, name='index'),
    path('login/', views.tarefas_login, name='login'),
    path('cadastro/', views.tarefas_cadastro, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.tarefas_home, name='home'),
    path('adicionar/', views.tarefas_adicionar, name='adicionar'),
    path('editar/<int:id>/', views.tarefas_editar, name='editar'),
    path('remover/<int:id>/', views.tarefas_remover, name='remover'),

]
