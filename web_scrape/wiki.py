#
# read the data from the URL and print it
#
import urllib3 
#from bs4 import BeautifulSoup4
from bs4 import BeautifulSoup

link = "https://en.wikipedia.org/wiki/Special:Random"

# open a connection to a URL using urllib
http = urllib3.PoolManager()
print("test")
r = http.request('GET', link)
r.data
#get the result code and print it

soup = BeautifulSoup(r.data, features='lxml')
article = soup.get_text()
#print(soup.get_text())
# read the data from the URL and print it

text = open('wikipedia.txt', 'w', encoding='utf-8')
text.write(article)
text.close() 
