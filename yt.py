from pytube import YouTube
import time

def main():

    print(" ")
    
main()

def display_options(stream):
    (f"Resolução: {stream.resolution}, Tipo: {stream.type}, Taxa de bits (abr): {stream.abr}")

def download_callback(stream, chunk, remaining):
    # Adiciona uma função de callback para verificar se o download foi concluído
    if remaining == 0:
        print("Download concluído.")

link = input("Cole o Link do Vídeo: ")

print('   ')
print('Aguarde...')
print('    ')
VIDEO_URL = link
('VERIFIQUE SEU LINK DE DOWNLOAD')
yt = YouTube(VIDEO_URL, on_progress_callback=download_callback)

# Mostra as opções de stream disponíveis para o vídeo com números
for i, stream in enumerate(yt.streams, start=1):
    display_options(stream)
    print(f"{i}. Resolução: {stream.resolution}, Tipo: {stream.type}, bits: {stream.abr}")

# Solicita ao usuário escolher a opção desejada para o download
opcao = int(input("Digite o número da opção desejada para download: "))

# Verifica se a opção é válida e faz o download
if 1 <= opcao <= len(yt.streams):
    video = yt.streams[opcao - 1]
    print('   ')
    print(f'Baixando vídeo...')
    print('   ')
    video.download()
else:
    print("Opção inválida. Escolha um número válido da lista acima.")
