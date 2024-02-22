import pytube.exceptions
from pytube import YouTube


def video_download(url, path):
    try:
        my_video = YouTube(url)
        my_video = my_video.streams.get_highest_resolution()
        my_video.download(output_path=path)
    except pytube.exceptions.RegexMatchError:
        print('An error has occured')



