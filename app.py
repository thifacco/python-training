import os

restaurantes = [
   {'nome': 'Maniva', 'ativo': True},
   {'nome': 'Café Garden', 'ativo': False},
   {'nome': 'Jacaré Madalena', 'ativo': True},
   {'nome': 'Fogo de Chão', 'ativo': False},
   {'nome': 'Marina Del Mare', 'ativo': True},
]

def voltar_menu_principal():
   input('\nPressione ENTER para continuar...')
   main()

def exibir_subtitulo(subtitulo):
   os.system('clear')
   print(f'{subtitulo}\n')

def cadastrar_restaurante():
   exibir_subtitulo('Cadastrar restaurante')
   nome_restaurante = input('Nome do restaurante: ')
   restaurantes.append(nome_restaurante)
   print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
   voltar_menu_principal()

def listar_restaurantes():
   exibir_subtitulo('Listar restaurantes')
   for restaurante in restaurantes:
      nome = restaurante['nome']
      ativo = restaurante['ativo']
      print(f'- {nome} | Ativo: {ativo}')
   voltar_menu_principal()

def exibir_nome_programa():
   # https://fsymbols.com/pt/geradores/
   print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def exibir_opcoes():
   print('1. Cadastrar restaurante')
   print('2. Listar restaurante')
   print('3. Ativar restaurante')
   print('4. Sair\n')

def finalizar_app():
    print('Encerrando o programa\n')
    os.system('clear')

def opcao_invalida():
   exibir_subtitulo('Opção inválida')
   voltar_menu_principal()

def escolher_opcoes():
   try:
      opcao_escolhida = int(input('Escolha uma opção: '))
      
      match opcao_escolhida:
         case 1:
            cadastrar_restaurante()
         case 2:
            listar_restaurantes()
         case 3:
            print('Ativar restaurantes')
         case 4:
            finalizar_app()
         case _:
            opcao_invalida()
   except:
      opcao_invalida()

def main():
   os.system('clear')
   exibir_nome_programa()
   exibir_opcoes()
   escolher_opcoes()

if __name__ == '__main__':
    main()