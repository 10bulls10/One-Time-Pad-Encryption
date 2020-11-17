#I'm trying to encrypt some stuff

key = 5

message = open("message.txt", "r")
content = message.read()
#print(content)
message.close()

lcon = len(content)

#message = open("copy.txt", "w")
#message.write(content)
#message.close()


shift = []
for i in range(0, len(content)):
    shift.append(ord(content[i]))
    #if (content[i] == ' '):
        #shift[i] = 120
    print(shift)

shifted = []
for i in range(0, len(shift)):
    shifted.append(shift[i] + key)
    shifted[i] = chr(shifted[i])
print(shifted)

file = open("encrypted.txt", "w")
for i in range(0, len(shifted)):
    file.write(shifted[i])

file.close()



