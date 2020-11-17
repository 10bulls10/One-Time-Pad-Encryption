#
#GO TO A RANDOM WIKIPEDIA ARTICLE, TAKE TEXT, 
#REMOVE ALL WEIRD CHARACTERS SO YOU JUST HAVE WORDS
#THEN CHOOSE SOME WORDS FROM IT TO SAVE TO A TEXT FILE
#OF RANDOM WORDS
#
import urllib3 
from bs4 import BeautifulSoup
import re
from string import digits


def ditchDashes(thing):
    thing = [sub.replace('-', ' ') for sub in thing]
    return thing

#those dashes look the same but they're different... 
def strDitchDashes(thing):
    thing = thing.replace('–', ' ')
    thing = thing.replace('-', ' ')
    return thing

#supposed to ignore single letter words
def ditchSingles(thing):
    pattern = ' [A-Za-z0-9] '
    return re.sub(pattern, ' ', thing)
     
#if a string has a lowercase then a capital letter split it up since its likely 2 words 
def ultimateSplit(thing):
    thing = re.split(" ", thing)
    return thing


def ditchListMarks(thing):
    thing = [''.join(x for x in i if x.isalpha()) for i in thing] 
    for i in thing: 
        if len(i)==1: 
            thing.remove(i) 
    return thing


def getSomeLongs(thing):
    prev = 10
    big = []
    i = 0
    while (i<len(thing)):
        if len(thing[i]) > prev:
            big.append(thing[i])
            prev = len(thing[i])
        i += 1
    return big

def ditchLongs(thing, bigthing):
    for i in thing:
        if i in bigthing:
            thing.remove(i)
    return thing

def ditchWhiteSpace(thing):
    noSpaces = []
    for word in thing:
        if word.isalpha():
            noSpaces.append(word)
    return noSpaces

def splitListCaps(thing):
    new = []
    
    print(new)

#removes instances of [edit] which show up frequently on wikipedia
def strDitchEdit(thing):
    thing = thing.replace('[edit]', '')
    return thing
    

link = "https://en.wikipedia.org/wiki/Atomic_Energy_Act_of_1946"

# open a connection to a URL using urllib
http = urllib3.PoolManager()
r = http.request('GET', link)

soup = BeautifulSoup(r.data, features='lxml')
article = soup.get_text()
print("Article Type after soup.get_text: ", type(article))


article = strDitchEdit(article)

article = ditchSingles(article)
article = ultimateSplit(article)
article = ditchListMarks(article)
article = ditchWhiteSpace(article)
print(len(article))



#This converts the produced list to a string and saves it
strticle = str(article)
strticle.encode(encoding='utf-8', errors='replace')
text = open('textrando.txt', 'w', encoding='utf-8')
text.write(strticle)
text.close() 
print("COMPLETE")
