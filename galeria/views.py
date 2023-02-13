from django.shortcuts import render

def index(request):       # recebe a requisição
    return render(request, 'galeria/index.html')    #após a requisição, vai apresentar o index.html


def imagem(request): 
    return render(request, 'galeria/imagem.html') #galeria pasta onde esta o arquivo html
    
