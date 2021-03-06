'''
Web scraper. Is currently in a file downloader config. To make this file more versatile you can use  Regular Expressions to
search the parsed html file. Thy can also be used to help format the download directory or data structure. 

Currently this is set up to download roughly 1,000 white papers and text files that are on the hacking site. to limit this you can specify 
the types of files to download or but it in a counting loop to run it for a proof of concept without acquiring many files.
'''
from urllib import request
import requests                         #request information from a webpage
from bs4 import BeautifulSoup           #tools to sort through HTML to grab specified data


def spider(url):
    counter=1
    html_code = requests.get(url)
    plain_text = html_code.text #html is in plain text
    soup = BeautifulSoup(plain_text, 'html.parser') #put meaning to the html tags
    for link in soup.find_all('a'): #loops through every <a tag gets the href link and passes the link to downloader function
        counter+=1
        if(counter>9):#skips first few links, this can be remmoved with reg expressions that better define the tags
            href = link.get('href')
            href_link = url+href
            downloader(href_link, href)

def downloader(href_link, href):#href will be the name of the file download, href_link will be used to download at that location
    print(href_link)
    dest_file= 'files/'+str(href)
    http_response = request.urlopen(href_link)
    txt_str = str(http_response.read())
    #ignores all newlines and tab characters and any other artifacts that are created by the parser
    lines = txt_str.split("\\n")
    fw = open(dest_file, 'w')
    for line in lines:
        line = line.strip("\\n")
        line = line.strip("\\r")
        line = line.replace("\\t", '')
        line = line.replace("\\'", '\'')
        fw.write(line + "\n")
    fw.close()


spider('http://www.textfiles.com/hacking/') #make me into a GUI or CUI!
