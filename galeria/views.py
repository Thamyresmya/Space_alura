from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):   # recebe a requisição 
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)         # filtro para aparecer publicações  # ordenação pelo mais recente  #mais antigo coloca o - na frente
    return render(request, 'galeria/index.html', {"cards": fotografias})    #após a requisição, vai apresentar o index.html


def imagem(request, foto_id): 
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia}) #galeria pasta onde esta o arquivo html

# função para busca
def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)   #busca todos os itens do BD
    
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)        # se alguma parte do nome da busca faz sentido com o nome   
    
    return render(request, 'galeria/buscar.html', {"cards": fotografias})            



