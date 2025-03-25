from modelos.avaliacao import Avaliacao

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

   def adicionar_bebida_cardapio(self, bebida):
      self._cardapio.append(bebida)
   
   def adicionar_prato_cardapio(self, prato):
      self._cardapio.append(prato)
   
