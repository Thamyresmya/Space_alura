from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'),          #pagina principal '' vazio, vai aparecer a função index
    path('imagem/', imagem, name='imagem'),
]
