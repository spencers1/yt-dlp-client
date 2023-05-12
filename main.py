import os

from yt_dlp import YoutubeDL

def download_video(video):
    print("video:" + video);
    URL = [video]
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(URL)

if __name__ == '__main__':
    dl_url = os.environ.get('DL_URL')
    download_video(dl_url)
