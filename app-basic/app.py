import os

restaurantes = [
   {'nome': 'Maniva', 'categoria': 'Gourmet', 'ativo': True},
   {'nome': 'Café Garden', 'categoria': 'Gormet', 'ativo': False},
   {'nome': 'Jacaré Madalena', 'categoria': 'Grill', 'ativo': True},
   {'nome': 'Fogo de Chão', 'categoria': 'Churrascaria', 'ativo': False},
   {'nome': 'Marina Del Mare', 'categoria': 'Italiano', 'ativo': True},
]

def exibir_nome_programa():
   '''Função que exibe o nome do programa'''
   os.system('clear')
   # https://fsymbols.com/pt/geradores/
   print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def exibir_subtitulo(subtitulo):
   '''
   Função que exibe um subtitulo na tela
   
   Inputs:
      - subtitulo: str
   '''
   os.system('clear')
   print(f'{subtitulo}')
   print('\n')

def voltar_menu_principal():
   '''Função que aguarda o usuário pressionar ENTER para voltar ao menu principal'''
   input('\nPressione ENTER para continuar...')
   main()

def cadastrar_restaurante():
   '''Função que cadastra um restaurante na lista de restaurantes'''
   exibir_subtitulo('Cadastrar restaurante')
   nome_restaurante = input('Nome do restaurante: ')
   categoria_restaurante = input('Categoria do restaurante: ')
   restaurantes.append({'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':False})
   print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
   voltar_menu_principal()

def listar_restaurantes():
   '''Função que lista os restaurantes cadastrados'''
   exibir_subtitulo('Listar restaurantes')
   print('Nome'.ljust(20), '| Categoria'.ljust(22), '| Estado')
   print('-'*60)
   for restaurante in restaurantes:
      nome = restaurante['nome']
      categoria = restaurante['categoria']
      ativo = 'ativo' if restaurante['ativo'] else 'inativo'
      print(f'{nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
   voltar_menu_principal()

def alternar_estado_restaurante():
   '''Função que altera o estado de um restaurante'''
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

def exibir_opcoes():
   '''Função que exibe as opções do menu principal'''
   print('1. Cadastrar restaurante')
   print('2. Listar restaurante')
   print('3. Alternar estado do restaurante')
   print('4. Sair\n')

def finalizar_app():
   '''Função que finaliza a aplicação'''
   print('Encerrando a aplicação\n')
   os.system('clear')

def opcao_invalida():
   '''Função que exibe uma mensagem de opção inválida'''
   exibir_subtitulo('Opção inválida')
   voltar_menu_principal()

def escolher_opcoes():
   '''Função que aguarda o usuário escolher uma opção'''
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
   '''Função principal'''
   exibir_nome_programa()
   exibir_opcoes()
   escolher_opcoes()

if __name__ == '__main__':
    main()