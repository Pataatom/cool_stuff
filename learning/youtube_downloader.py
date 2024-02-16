import requests
import youtube_dl

def get_video_title(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, False)
    return info_dict["title"]

url = input(f"url> ")
print(get_video_title(url))
request = requests.get(url)
# with open()