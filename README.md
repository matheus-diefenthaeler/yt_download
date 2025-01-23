# YouTube Video Downloader

Este projeto é um aplicativo simples de linha de comando, utilizando a biblioteca `yt-dlp`, para realizar o download de vídeos do YouTube com diferentes resoluções. Ele foi desenvolvido usando a biblioteca `tkinter` para a interface gráfica.

## Recursos
- Download de vídeos do YouTube diretamente a partir de uma URL.
- Opções de resolução (720p, 480p, 360p, 1080p, Máximo disponível).
- Interface gráfica desenvolvida com `tkinter` para facilitar a interação do usuário.
- Configuração de progresso de download.

## Pré-requisitos
Antes de executar o programa, você precisa ter as seguintes dependências instaladas:
- `python` (versão 11)
- `yt-dlp` (biblioteca de download do YouTube)
- `tqdm` (biblioteca para exibição de progresso)
- `ffmpeg` (ferramenta de conversão de mídia, necessária para a conversão de vídeo para MP4)

Você pode instalar essas dependências usando o seguinte comando no terminal:
```bash
pip install -r requirements.txt
```


## Instalação do ffmpeg e adição ao PATH:
### 1 Baixar o ffmpeg:

- Acesse o site oficial do ffmpeg e baixe a versão estável para o seu sistema operacional (Windows, macOS ou Linux).

### 2 Extrair o arquivo:

- Após o download, extraia o conteúdo para um local acessível, como C:\ffmpeg (para Windows) ou /usr/local/ffmpeg (para macOS/Linux).

### 3 Adicionar ao PATH:

- Pressione Win + R para abrir o Executar.
- Digite env e pressione Enter para abrir o Editor de Variáveis de Ambiente.
- Clique em Variáveis do Sistema e procure por Path.
- Clique em Novo e insira o caminho onde o ffmpeg foi extraído (C:\ffmpeg\bin).
- Clique em OK para confirmar.

### 4 Verificar instalação:
- ffmpeg -version

## Gerando o executável:
Para gerar o executável (.exe) do projeto, você pode utilizar o PyInstaller. Após instalar todas as dependências corretamente, execute o seguinte comando no terminal:
```bash
pyinstaller --onefile --noconsole main.py
```

## Compartilhando o executável:
- Compartilhe as pastas dist e build para que outros usuários possam executar o programa.
- Garanta que a pessoa que receber o executável tenha os pré-requisitos básicos (como Python e ffmpeg instalado).
