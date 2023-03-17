from django.urls import path

from . import views

app_name = 'disciplina'

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar')
    
]
