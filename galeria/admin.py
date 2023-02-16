from django.contrib import admin
from galeria.models import Fotografia



class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome")     #lugares que sejam links pra levar a itens espeficicos
    search_fields = ("nome", )              #vai aparecer um campo de busca
    list_filter = ("categoria", )           #filtrar por categoria
    list_editable = ("publicada", )         #mostra no display para marcar ou nao
    list_per_page = 10                      #lista 10 itens por pagina
    
    
    
        
#todas as modificações tem que colocar o paramentro, aquï é onde mostrar no BD admin
admin.site.register(Fotografia, ListandoFotografias)



