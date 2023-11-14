import re
import os
import importlib


def menu_principal():
    print("Qual a plataforma deseja usar?")
    print("     ")
    print("1 - Scribd")
    print("2 - Passei Direto")
    print("3 - Instagram - Video")
    print("4 - YouTube")
    print("0 - Sair")
    print("     ")

def submenu_scribd():
    print("     ")
    print("-------Scribd--------")
    print("     ")
    print("1 - Gerar Link")
    print("2 - Abrir Navegador")
    print("3 - Voltar ao menu principal")
    print("     ")

def submenu_pd():
    print("     ")
    print("------Passei Direto------")
    print("     ")
    print("1 - Desabilitado")
    print("2 - Desabilitado")
    print("3 - Voltar ao menu principal")
    print("     ")
    
def submenu_youtube():
        print("     ")
        print("------Youtube------")
        print("     ")
        print("1 - Video e Audio")
        print("2 - PlayList")
        print("3 - Voltar ao menu principal")
        print("     ")
    
def submenu_insta():
        print("     ")
        print("-------Download Video--------")
        print("     ")
        print("1 - Gerar Link")
        print("0 - Voltar ao menu principal")
        print("     ")

# Função principal
def main():
    while True:
        menu_principal()
        opcao_principal = input("Escolha uma opção: ")

        if opcao_principal == "1":
            while True:
                submenu_scribd()
                opcao_fotos = input("Escolha uma opção: ")

                if opcao_fotos == "1":
                    print("     ")


                     # Importação do arquivo scrib.py
                    nome_do_modulo = "scrib"
                    modulo_importado = importlib.import_module(nome_do_modulo)
                    
                    # Chamar a função main() do módulo scrib.py
                    modulo_importado.main()

                elif opcao_fotos == "2":
                    print("     ")
                    print("Em fase de testes!")
                    # Coloque aqui o código para editar fotos

                elif opcao_fotos == "3":
                    break  # Volta ao menu principal

                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao_principal == "2":
            while True:
                submenu_pd()
                opcao_link = input("Escolha uma opção: ")

                if opcao_link == "1":
                    print("Null")
                    # Coloque aqui o código para editar o link

                elif opcao_link == "2":
                    print("Null")
                    # Coloque aqui o código para copiar o link

                elif opcao_link == "3":
                    break  # Volta ao menu principal

                else:
                    print("Opção inválida. Tente novamente.")
                    
        elif opcao_principal == "3":
            while True:
                submenu_insta()
                opcao_link = input("Escolha uma opção: ")

                if opcao_link == "1":
                    print("     ")
                    # Coloque aqui o código para editar o link
                    # Importação do arquivo 
                    nome_do_modulo = "insta"
                    modulo_importado = importlib.import_module(nome_do_modulo)
                    

                    database_connection.close()

                    # Chamar a função main() do módul
                    modulo_importado.main()


                elif opcao_link == "2":
                    print("Null")
                    # Coloque aqui o código para copiar o link

                elif opcao_link == "0":
                    break  # Volta ao menu principal

                else:
                    print("Opção inválida. Tente novamente.")
                    
        elif opcao_principal == "4":
            while True:
                submenu_youtube()
                opcao_link = input("Escolha uma opção: ")

                if opcao_link == "1":
                    print("     ")
                    # Coloque aqui o código para editar o link
                    # Importação do arquivo 
                    nome_do_modulo = "yt"
                    modulo_importado = importlib.import_module(nome_do_modulo)
                    

                    database_connection.close()

                    # Chamar a função main() do módul
                    modulo_importado.main()

                elif opcao_link == "2":
                    print("    ")
                    # Coloque aqui o código para copiar o link
                    nome_do_modulo = "play"
                    modulo_importado = importlib.import_module(nome_do_modulo)
                    

                    database_connection.close()

                    # Chamar a função main() do módul
                    modulo_importado.main()

                elif opcao_link == "3":
                    break  # Volta ao menu principal

                else:
                    print("Opção inválida. Tente novamente.")            

        elif opcao_principal == "0":
            print("Saindo...")
            break  # Encerra o programa

        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal
main()
