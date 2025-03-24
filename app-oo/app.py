from modelos.restaurante import Restaurante

restaurante_maniva = Restaurante('Maniva', 'Brasileira')
restaurante_cafe_garden = Restaurante('Café Garden', 'Gourmet')
restaurante_cafe_garden.alternar_estado()
restaurante_jacare_madalena = Restaurante('Jacaré Madalena', 'Grill')

def main():
   Restaurante.listar_restaurantes()

if __name__ == '__main__':
   main()