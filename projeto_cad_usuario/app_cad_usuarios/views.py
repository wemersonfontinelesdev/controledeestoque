from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
  return render(request,'usuarios/home.html')
""""
def usuarios(request):
    # Salvar os dados do formulário no banco de dados, se o método for POST
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()"""

def usuarios(request):
    # Salvar os dados do formulário no banco de dados, se o método for POST
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.descricao = request.POST.get('descricao')
        novo_usuario.quantidade = request.POST.get('quantidade')

        # Salvando a foto, se houver
        if 'foto' in request.FILES:
            novo_usuario.foto = request.FILES['foto']

        novo_usuario.save()

# Recuperar todos os usuários cadastrados
    todos_usuarios = Usuario.objects.all()

# Retornar os dados para a página da listagem de usuários
    return render(request, 'usuarios/usuarios.html', {'usuarios': todos_usuarios})
