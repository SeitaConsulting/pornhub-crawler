from bs4 import BeautifulSoup
import re
import time
import urllib.request

if __name__ == '__main__':
    page = 1
    url = 'https://www.pornhub.com/pornstars?page='
    while page < 1773: #Check your self!
        html = urllib.request.urlopen(url + str(page)).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.select("a[class='title js-mxp']")
        url2 = 'https://www.pornhub.com'
        for element in elements:
            try:
                #print(element['href'])
                html2 = urllib.request.urlopen(url2 + element['href']).read().decode('utf-8')
                soup2 = BeautifulSoup(html2, 'html.parser')
                element2 = soup2.select_one("[itemprop='height']") #property
                height = int(re.findall("(?<=\().+?(?=\))", element2.get_text())[0].replace(' ', '').replace('cm', '')) #remove unit
                if height <= 163: #value
                    with open('./list.txt', 'a') as f: #Set your own path!
                        print(url2 + element['href'], file=f)
                time.sleep(5)
            except:
                pass
        page += 1
