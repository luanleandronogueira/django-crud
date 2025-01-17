from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, update, excluir

urlpatterns = [
    path('', home),
    path('salvar', salvar, name = 'salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('excluir/<int:id>', excluir, name='excluir')
]