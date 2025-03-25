from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
   Restaurantes = []
   
   # método construtor (especial)
   def __init__(self, nome, categoria):
      self._nome = nome.title()
      self._categoria = categoria.upper()
      self._ativo = False
      self._avaliacao = []
      self._cardapio = []
      Restaurante.Restaurantes.append(self)
   
   # método para exibir o objeto em formato texto (especial)
   def __str__(self):
      return f"Restaurante {self._nome} | Categoria {self._categoria} | Ativo: {self.ativo}"
   
   # método para listar o restaurante (próprio)
   @classmethod
   def listar_restaurantes(cls):
      print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} Status')
      for restaurante in cls.Restaurantes:
         print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
   
   @property
   def ativo(self):
      return '✅' if self._ativo == True else '❌'

   def alternar_estado(self):
      self._ativo = not self._ativo
   
   def receber_avaliacao(self, cliente, nota):
      avaliacao = Avaliacao(cliente, nota)
      self._avaliacao.append(avaliacao)
   
   @property
   def media_avaliacoes(self):
      if not self._avaliacao:
         return 0
      
      soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
      quantidade_de_notas = len(self._avaliacao)
      media = round(soma_das_notas / quantidade_de_notas, 1)
      
      return media

   def adicionar_cardapio(self, item):
      if isinstance(item, ItemCardapio):
         self._cardapio.append(item)
   
   # código omitido

   @property
   def exibir_cardapio(self):
      print(f'Cardapio do restaurante {self._nome}\n')
      for i,item in enumerate(self._cardapio,start=1):
         if hasattr(item,'descricao'):
            mensagem_prato = f'{i}. Nome: {item._nome.ljust(20)} | Preço: R${str(item._preco).ljust(10)} | Descrição: {item.descricao}'
            print(mensagem_prato)
         elif hasattr(item,'tamanho'):
            mensagem_bebida = f'{i}. Nome: {item._nome.ljust(20)} | Preço: R${str(item._preco).ljust(10)} | Tamanho: {item.tamanho}'
            print(mensagem_bebida)
         elif hasattr(item,'diet'):
            mensagem_sobremesa = f'{i}. Nome: {item._nome.ljust(20)} | Preço: R${str(item._preco).ljust(10)} | Diet: {item.diet}'
            print(mensagem_sobremesa)