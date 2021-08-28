from pytube import YouTube
from pytube.cli import on_progress

yt = YouTube('https://www.youtube.com/watch?v=jfvB3DPJ4FU', on_progress_callback=on_progress)
print(yt.title)

stream = yt.streams
print(yt.streams.filter(progressive=True).first())
#print(yt.streams.first())
#stream = yt.streams.get_by_itag(140)
#print(stream.filesize)
#stream.download()


# 139 140 249 250 251