#just gonna scramble some words

block = open("random1.txt", "r", encoding='utf-8')
random1 = block.read()
block.close()

random1.encode(encoding='utf-8', errors='replace')

text = random1.split(sep=None, maxsplit=-1)

print(len(random1))
print(len(text))
print(text[3000:3004]) #test print
print(text[3000])
print(text[3000][0])

gaps = len(text)/8
gaps = int(gaps)
test = []
for i in range (0, 8):
    test.append(text[gaps*i:gaps*(i+1)])

#set1 = text[:gaps]
#set2 = text[gaps:2*gaps]

#
test = zip(set1, set2)
print(list(test))


