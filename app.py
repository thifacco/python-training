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

def escolher_opcoes():
   opcao_escolhida = int(input('Escolha uma opção: '))
   
   if opcao_escolhida == 1:
      print('Cadastrar restaurante')
   elif opcao_escolhida == 2:
      print('Listar restaurantes')
   elif opcao_escolhida == 3:
      print('Ativar restaurantes')
   else:
      finalizar_app()

def main():
   exibir_nome_programa()
   exibir_opcoes()
   escolher_opcoes()

if __name__ == '__main__':
    main()