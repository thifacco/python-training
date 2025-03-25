from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_marie = Restaurante('Marie', 'Mediterrânea')
bebida_sangria = Bebida('Sangria de Frutas', 35.0, 'médio')
prato_macarrao = Prato('Macarrão Al Mare', 2.00, 'Massa com frutos do mar')
restaurante_marie.adicionar_bebida_cardapio(bebida_sangria)
restaurante_marie.adicionar_prato_cardapio(prato_macarrao)

def main():
   print(bebida_sangria)
   print(prato_macarrao)

if __name__ == '__main__':
   main()