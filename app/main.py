import os
import tkinter as tk
from tkinter import messagebox

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

    def _hook(self, d):
        """Método para atualizar a barra de progresso (não utilizado diretamente com tkinter no momento)."""
        if d['status'] == 'downloading':
            if d.get('total_bytes') is not None:
                self.progress.set(d['downloaded_bytes'] / d['total_bytes'])

    def download_video(self, url, resolution):
        try:
            # Aqui o map continua, mas o formato usado é mais genérico e funcional
            resolution_map = {
                '1': 'bestvideo[height<=720]+bestaudio/best',
                '2': 'bestvideo[height<=480]+bestaudio/best',
                '3': 'bestvideo[height<=360]+bestaudio/best',
                '4': 'bestvideo[height<=1080]+bestaudio/best',
                '5': 'bestvideo+bestaudio/best'  # Máximo disponível
            }
            video_format = resolution_map.get(resolution, resolution_map['1'])

            ydl_opts = {
                'format': video_format,
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'noplaylist': True,
                'merge_output_format': 'mkv',  # MKV lida melhor com diferentes codecs
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Baixando vídeo de: {url}")
                ydl.download([url])
                messagebox.showinfo("Download Concluído", "Download concluído! Arquivo salvo como MKV.")
        except yt_dlp.utils.DownloadError as e:
            messagebox.showerror("Erro", f"Erro ao tentar baixar o vídeo: {e}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Video Downloader")
        self.geometry("400x300")

        self.label_url = tk.Label(self, text="Digite a URL do vídeo:")
        self.label_url.pack(pady=10)

        self.entry_url = tk.Entry(self, width=50)
        self.entry_url.pack(pady=10)

        self.label_resolution = tk.Label(self, text="Escolha a resolução para download:")
        self.label_resolution.pack(pady=10)

        self.resolution_var = tk.StringVar(value='1')

        self.radio_button_720p = tk.Radiobutton(self, text="720p", variable=self.resolution_var, value='1')
        self.radio_button_720p.pack(anchor='w')

        self.radio_button_480p = tk.Radiobutton(self, text="480p", variable=self.resolution_var, value='2')
        self.radio_button_480p.pack(anchor='w')

        self.radio_button_360p = tk.Radiobutton(self, text="360p", variable=self.resolution_var, value='3')
        self.radio_button_360p.pack(anchor='w')

        self.radio_button_1080p = tk.Radiobutton(self, text="1080p", variable=self.resolution_var, value='4')
        self.radio_button_1080p.pack(anchor='w')

        self.radio_button_max = tk.Radiobutton(self, text="Máximo disponível", variable=self.resolution_var, value='5')
        self.radio_button_max.pack(anchor='w')

        self.download_button = tk.Button(self, text="Baixar", command=self.start_download)
        self.download_button.pack(pady=20)

    def start_download(self):
        video_url = self.entry_url.get()
        resolution_choice = self.resolution_var.get()

        if not video_url:
            messagebox.showwarning("Advertência", "Por favor, insira a URL do vídeo.")
            return

        downloader = YouTubeDownloader(download_path='./downloads')
        downloader.download_video(video_url, resolution_choice)


if __name__ == "__main__":
    app = App()
    app.mainloop()
