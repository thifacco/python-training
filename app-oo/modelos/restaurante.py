class Restaurante:
   def __init__(self, nome, categoria):
    self.nome = nome
    self.categoria = categoria
    self.ativo = False
   
   def __str__(self):
    return f"Restaurante {self.nome} | Categoria {self.categoria} | Ativo: {self.ativo}"
    
restaurante_praca = Restaurante('Restaurante da Praça', 'Prato Feito')

# imprime as propriedades do objeto
print(dir(restaurante_praca))

# imprime os atributos do objeto
print(vars(restaurante_praca))

# imprime o valor de um atributo específico
print(restaurante_praca.nome)

# mostra o objeto em formato texto
print(restaurante_praca)