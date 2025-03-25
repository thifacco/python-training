from modelos.avaliacao import Avaliacao

class Restaurante:
   Restaurantes = []
   
   # método construtor (especial)
   def __init__(self, nome, categoria):
      self._nome = nome.title()
      self._categoria = categoria.upper()
      self._ativo = False
      self._avaliacao = []
      Restaurante.Restaurantes.append(self)
   
   # método para exibir o objeto em formato texto (especial)
   def __str__(self):
      return f"Restaurante {self._nome} | Categoria {self._categoria} | Ativo: {self.ativo}"
   
   # método para listar o restaurante (próprio)
   @classmethod
   def listar_restaurantes(cls):
      print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | Status')
      for restaurante in cls.Restaurantes:
         print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |  {restaurante.ativo}')
   
   @property
   def ativo(self):
      return '✅' if self._ativo == True else '❌'

   def alternar_estado(self):
      self._ativo = not self._ativo
   
   def receber_avaliacao(self, cliente, nota):
      avaliacao = Avaliacao(cliente, nota)
      self._avaliacao.append(avaliacao)
