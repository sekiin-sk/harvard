import re
import os

def main():
    # Solicite o link ao usuário
    link = input("Insira o link: ")

    # Encontre a string "pt.scribd" no link
    pt_scribd = re.search(r"pt.scribd", link)

    # Se a string for encontrada, substitua-a por "scribd.vdownloaders"
    if pt_scribd:
        link = link.replace(pt_scribd.group(), "scribd.vdownloaders")


 # Limpa a tela
    print("\x1b[2J")


    # Imprima o novo link
    print("Acesse o novo link e faça o download do arquivo do Scribd:")
    print(link)

    # Pausa
    input("Pressione Enter para continuar...")

    # Limpa a tela
    print("\x1b[2J")

    # Retorne para a linha "Solicite o link ao usuário"
    return

if __name__ == "__main__":
    main()
