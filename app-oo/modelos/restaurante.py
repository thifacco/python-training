class Restaurante:
   Restaurantes = []
   
   # método construtor (especial)
   def __init__(self, nome, categoria):
    self.nome = nome
    self.categoria = categoria
    self._ativo = False
    Restaurante.Restaurantes.append(self)
   
   # método para exibir o objeto em formato texto (especial)
   def __str__(self):
    return f"Restaurante {self.nome} | Categoria {self.categoria} | Ativo: {self.ativo}"
   
   # método para listar o restaurante (próprio)
   def listar_restaurantes():
    for restaurante in Restaurante.Restaurantes:
        print(f'Nome: {restaurante.nome} | Categoria: {restaurante.categoria} | Ativo: {restaurante.ativo}')
   
   @property
   def ativo(self):
    return '✅' if self._ativo == True else '❌'
    
restaurante_praca = Restaurante('Restaurante da Praça', 'Prato Feito')

# imprime as propriedades do objeto
print(dir(restaurante_praca))

# imprime os atributos do objeto
print(vars(restaurante_praca))

# imprime o valor de um atributo específico
print(restaurante_praca.nome)

# mostra o objeto em formato texto
print(restaurante_praca)

# chama o método listar_restaurantes
Restaurante.listar_restaurantes()