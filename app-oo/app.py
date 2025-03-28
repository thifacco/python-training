from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.sobremesa import Sobremesa

restaurante_marie = Restaurante('Marie', 'Cozinha Mediterrânea')

bebida_sangria = Bebida('Sangria de Frutas', 25.0, 'médio')
bebida_sangria.aplicar_desconto()
restaurante_marie.adicionar_cardapio(bebida_sangria)

prato_macarrao = Prato('Pasta Al Mare', 80.00, 'Massa com frutos do mar')
prato_macarrao.aplicar_desconto()
restaurante_marie.adicionar_cardapio(prato_macarrao)

sobremesa_petitgateau = Sobremesa('Pettit Gateau', 20.00, 'sim')
sobremesa_petitgateau.aplicar_desconto()
restaurante_marie.adicionar_cardapio(sobremesa_petitgateau)

def main():
   restaurante_marie.exibir_cardapio

if __name__ == '__main__':
   main()