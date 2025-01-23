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
            format_choice = input("Digite o número do formato: ")

            # Solicita ao usuário a resolução desejada
            print("Escolha a resolução para download:")
            print("1. 720p (Alta qualidade)")
            print("2. 480p (Qualidade média)")
            print("3. 360p (Qualidade baixa)")
            resolution_choice = input("Digite o número da resolução: ")

            # Define o formato com base na escolha do usuário
            if format_choice == '1':
                extension = '.mp4'
                base_format = 'mp4'
            elif format_choice == '2':
                extension = '.webm'
                base_format = 'webm'
            else:
                print("Escolha inválida! O formato padrão será MP4.")
                extension = '.mp4'
                base_format = 'mp4'

            # Define a resolução com base na escolha do usuário
            resolution_map = {
                '1': 'bestvideo[height<=720][ext=' + base_format + ']+bestaudio[ext=m4a]/' + base_format,
                '2': 'bestvideo[height<=480][ext=' + base_format + ']+bestaudio[ext=m4a]/' + base_format,
                '3': 'bestvideo[height<=360][ext=' + base_format + ']+bestaudio[ext=m4a]/' + base_format,
            }
            video_format = resolution_map.get(resolution_choice, resolution_map['1'])  # Default para 720p

            # Configurações do yt-dlp
            ydl_opts = {
                'format': video_format,  # Define o formato com base em resolução e tipo
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
