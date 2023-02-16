from django.db import models
from datetime import datetime 

class Fotografia(models.Model):
    
    #criar uma lista de categorias:
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),      
    ]    
    
    # nomes das colunas do banco de dados
    nome = models.CharField(max_length=100, null=False, blank=False)                  #não pode ser nulo e nem string vazia
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')     #choices => forma de incluir uma lista para escolha
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)                 #local onde sera salvo as fotos sera salvo em uma pasta de ano e outra de dia
    publicada = models.BooleanField(default=False)                                 #esperar para ainda publicar
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)      #incluir data atual do cadastro
       
        
    def __str__(self):
        return self.nome             #aparecer nome lá no db
