from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_marie = Restaurante('Marie', 'Cozinha Mediterrânea')
bebida_sangria = Bebida('Sangria de Frutas', 35.0, 'médio')
prato_macarrao = Prato('Macarrão Al Mare', 2.00, 'Massa com frutos do mar')
restaurante_marie.adicionar_cardapio(bebida_sangria)
restaurante_marie.adicionar_cardapio(prato_macarrao)

def main():
   restaurante_marie.exibir_cardapio

if __name__ == '__main__':
   main()