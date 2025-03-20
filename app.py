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
   print(f'{subtitulo}')
   print('\n')

def cadastrar_restaurante():
   exibir_subtitulo('Cadastrar restaurante')
   nome_restaurante = input('Nome do restaurante: ')
   restaurantes.append({'nome':nome_restaurante, 'ativo':False})
   print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
   voltar_menu_principal()

def listar_restaurantes():
   exibir_subtitulo('Listar restaurantes')
   print('Nome'.ljust(20), '| Estado')
   print('-'*30)
   for restaurante in restaurantes:
      nome = restaurante['nome']
      ativo = 'ativo' if restaurante['ativo'] else 'inativo'
      print(f'{nome.ljust(20)} | {ativo}')
   voltar_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
      print('O restaurante não foi encontrado.')  
        
    voltar_menu_principal()

def exibir_nome_programa():
   # https://fsymbols.com/pt/geradores/
   print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def exibir_opcoes():
   print('1. Cadastrar restaurante')
   print('2. Listar restaurante')
   print('3. Alternar estado do restaurante')
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
            alternar_estado_restaurante()
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