from pytube import YouTube, Playlist
from tqdm import tqdm
import os
import requests

def main():

    print(" ")
    
main()

def download_with_progress(url, output_path='.', chunk_size=8192):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    bar = tqdm(total=total_size, unit='B', unit_scale=True, desc="Baixando")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Certifica-se de que o diretório de saída existe

    with open(output_path, 'wb') as file, requests.get(url, stream=True) as response:
        for data in response.iter_content(chunk_size=chunk_size):
            bar.update(len(data))
            file.write(data)

    bar.close()

link = input("Cole o Link da Playlist: ")

PLAYLIST_URL = link
playlist = Playlist(PLAYLIST_URL)
print('   ')
print('Você concorda em fazer o download de todos os vídeos da playlist na melhor qualidade disponível?')
print('   ')

confirmacao = input("Digite '1' para concordar ou '2' para cancelar: ")

if confirmacao == '1':
    print('Aguarde...')
    for url in playlist:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        output_file = os.path.join('playlist', f'{video.title}.mp4')
        download_with_progress(stream.url, output_file)

    print('Download concluído!')
else:
    print('Download cancelado pelo usuário.')
