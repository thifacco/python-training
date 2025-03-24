class Restaurante:
   def __init__(self, nome, categoria):
    self.nome = nome
    self.categoria = categoria
    self.ativo = False
    
restaurante_praca = Restaurante('Restaurante da Praça', 'Prato Feito')

# imprime os atributos do objeto
print(vars(restaurante_praca))

# imprime o valor de um atributo específico
print(restaurante_praca.nome)