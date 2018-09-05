'''
File downloader, mix with a web crawler to fill in files names and paths.
'''

from urllib import request
#put your file to download here
txt_url = 'http://www.textfiles.com/hacking/2600-9-3.txt'
#File to save to here
dest_file = r'2006_Mag.txt'#r for raw string so it will save to directory paths correctly

def downloader(txt_url):
    response = request.urlopen(txt_url)
    txt_str = str(response.read())
    lines = txt_str.split("\\n")
    fw = open(dest_file, 'w')
    for line in lines:
        line = line.strip("\\n")
        line = line.strip("\\r")
        line = line.replace("\\t", '')
        line = line.replace("\\'", '\'')
        fw.write(line + "\n")
    fw.close()

downloader(txt_url)