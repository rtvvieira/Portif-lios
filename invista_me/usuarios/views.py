from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def novo_usuario(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            mensagem = messages.success(
                request, f'o usuario {usuario} foi criado com sucesso!')
            return redirect('login')

    else:
        formulario = UserRegisterForm()

    return render(request, 'usuarios/registrar.html', {'formulario': formulario})
