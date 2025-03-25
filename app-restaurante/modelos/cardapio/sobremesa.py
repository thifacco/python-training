from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
   def __init__(self, nome, preco, diet):
      super().__init__(nome, preco)
      self.diet = diet
   
   def aplicar_desconto(self):
      self._preco -= (self._preco * 0.1)