from django.shortcuts import render
from .models import Usuario
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.sobreome = request.POST.get('sobrenome')
    novo_usuario.data = request.POST.get('data')
    novo_usuario.fone = request.POST.get('fone')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.save()
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request,'usuarios/usuarios.html',usuarios)