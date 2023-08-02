import youtube_dl

url_link = 'link/to/video'

ydl_opts = {'outtmpl': f'video/video-1.webm'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url_link])
