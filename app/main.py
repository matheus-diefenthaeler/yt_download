import os
import yt_dlp

class YouTubeDownloader2:
    def __init__(self, download_path='./downloads'):
        """Inicializa o downloader com o caminho onde os vídeos serão salvos."""
        self.download_path = download_path
        self._ensure_download_path_exists()

    def _ensure_download_path_exists(self):
        """Garante que o diretório de download existe."""
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

    def download_video(self, url):
        """Realiza o download de um vídeo do YouTube a partir de uma URL."""
        try:
            # Solicita ao usuário o formato do vídeo desejado
            print("Escolha o formato para download:")
            print("1. MP4")
            print("2. WEBM")
            choice = input("Digite o número do formato: ")

            # Define o formato com base na escolha do usuário
            if choice == '1':
                video_format = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'
                extension = '.mp4'
            elif choice == '2':
                video_format = 'bestvideo[ext=webm]+bestaudio[ext=webm]/webm'
                extension = '.webm'
            else:
                print("Escolha inválida! O formato padrão será MP4.")
                video_format = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'
                extension = '.mp4'

            # Configurações do yt-dlp
            ydl_opts = {
                'format': video_format,  # Define o formato dinâmico
                'outtmpl': os.path.join(self.download_path, f'%(title)s{extension}'),  # Nome do arquivo com extensão escolhida
                'noplaylist': True,  # Não baixar playlists, apenas o vídeo
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Baixando vídeo de: {url}")
                ydl.download([url])
                print(f"Download concluído! Arquivo salvo em formato {extension}.")
        except yt_dlp.utils.DownloadError as e:
            print(f"Erro ao tentar baixar o vídeo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    print("=== YouTube Video Downloader com yt-dlp ===")
    video_url = input("Digite a URL do vídeo do YouTube: ")

    downloader = YouTubeDownloader2(download_path='./downloads')
    downloader.download_video(video_url)
