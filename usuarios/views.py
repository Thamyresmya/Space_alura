from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:                                               # se nao é nome deu certo e faz login      
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    form = CadastroForms()   # Variavel que vai receber o form // inicialização
   
    if request.method == 'POST':
        form = CadastroForms(request.POST)     #vai pegar as informações do formulario e vai colocar dentro de um formulario novo
        
        if form.is_valid():                                                  # se as informações estão validas
            if form["senha_1"].value() != form["senha_2"].value():           #valida se as senhas são iguais e retorna para pag cadastro novamente
                messages.error(request, "Senhas não são iguais")
                return redirect('cadastro')                                  #passa o nome da rota que pretende ir
            
            nome=form["nome_cadastro"].value()                               #coloca os nomes iguais ao que esta no froms
            email=form["email"].value()                                      #pega as informações do form e colca em variaveis
            senha=form["senha_1"].value()            
            
            if User.objects.filter(username=nome).exists():                 #verificando se existe no BD
                messages.error(request, "Usuario já cadastrado")
                return redirect('cadastro')
            
            usuario = User.objects.create_user(                             #criando um novo usuario
                    username=nome,
                    email=email,
                    password=senha                              
            )
            usuario.save()                                                 #para salvar no BD
            messages.success(request, "Cadastro efetuado com sucesso")
            return redirect('login')
            
    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')


