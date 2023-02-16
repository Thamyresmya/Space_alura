from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'),          #pagina principal '' vazio, vai aparecer a função index
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name='buscar'),
]
