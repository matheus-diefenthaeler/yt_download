import os
import yt_dlp

class YouTubeDownloader:
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
            # Solicita ao usuário a resolução desejada
            print("Escolha a resolução para download:")
            print("1. 720p (Alta qualidade)")
            print("2. 480p (Qualidade média)")
            print("3. 360p (Qualidade baixa)")
            print("4. 1080p (Full HD)")
            print("5. O máximo disponível")
            resolution_choice = input("Digite o número da resolução: ")

            # Define a resolução com base na escolha do usuário
            resolution_map = {
                '1': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/mp4',
                '2': 'bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/mp4',
                '3': 'bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]/mp4',
                '4': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/mp4',
                '5': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Máximo disponível
            }
            video_format = resolution_map.get(resolution_choice, resolution_map['1'])  # Default para 720p

            # Configurações do yt-dlp com conversão forçada para MP4
            ydl_opts = {
                'format': video_format,  # Sempre tenta MP4
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),  # Nome do arquivo
                'noplaylist': True,  # Não baixar playlists, apenas o vídeo
                'merge_output_format': 'mp4',  # Conversão para MP4
                'postprocessors': [
                    {
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mp4'
                    }
                ],
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Baixando vídeo de: {url}")
                ydl.download([url])
                print("Download concluído! Arquivo salvo como MP4.")
        except yt_dlp.utils.DownloadError as e:
            print(f"Erro ao tentar baixar o vídeo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    print("=== YouTube Video Downloader com yt-dlp ===")
    video_url = input("Digite a URL do vídeo do YouTube: ")

    downloader = YouTubeDownloader(download_path='./downloads')
    downloader.download_video(video_url)
