import os

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
   print('Opção inválida\n')
   input('Pressione ENTER para continuar...')
   main()

def escolher_opcoes():
   try:
      opcao_escolhida = int(input('Escolha uma opção: '))
      
      match opcao_escolhida:
         case 1:
            print('Cadastrar restaurante')
         case 2:
            print('Listar restaurantes')
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