import re

test_list = ['hello', 'goodMorning', 'to', 'youHave', 'wandering-happily']
test_string = 'Hello! I hopeGood you are having a wonderful day-today.'
print('test_list: ', test_list, type(test_list))
print('test_string: ', test_string, type(test_string))


test_string = test_string.split()
print(test_string, type(test_string))
print(test_string[2])

test_string[2] = test_string[2].split("G")
print(test_string)


'''
wikipediaArticle = open("wikipedia.txt", "r")
article = wikipediaArticle.read()
print("Article type: ", type(article))

output = ' '
saved = open("regexTEST.txt", "w")
saved.write(output)
saved.close()
print("COMPLETE")
'''