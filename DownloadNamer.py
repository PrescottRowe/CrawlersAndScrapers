import random
import urllib.request

def download_web_image(url):
    name=random.randrange(10,000)
    full_name = str(name)+".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("")#put image url here and it will download the image to the same directory.
#connect this to a web crawler to download a bunch of images