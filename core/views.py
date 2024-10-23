from django.shortcuts import render, redirect
from .models import Pessoa

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {"pessoas": pessoas})

def salvar(request):
    nome = request.POST.get("nome_pessoa")
    Pessoa.objects.create(nome_pessoa=nome)
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id = id)
    return render(request, "update.html", {'pessoa': pessoa})

def update(request, id):
    nome = request.POST.get("nome_pessoa").upper()
    pessoa = Pessoa.objects.get(id = id)
    pessoa.nome_pessoa = nome
    pessoa.save()
    return redirect(home)

def excluir(request, id):
    pessoa = Pessoa.objects.get(id = id)
    pessoa.delete()
    return redirect(home)

    
