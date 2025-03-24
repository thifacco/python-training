class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Restaurante da Praça'
restaurante_praca.categoria = 'Prato Feito'
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

# imprime o objeto completo
print(dir(restaurantes))

# imprime os atributos do objeto
print(vars(restaurante_praca))

# imprime o valor de um atributo específico
print(restaurante_praca.nome)