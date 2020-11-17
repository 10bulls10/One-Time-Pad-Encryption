
key = 5
message = open("encrypted.txt", "r")
encrypted = message.read()
message.close()
print(encrypted)
print("DECRYPTED: ", "  ")

decrypt = []
for i in range(0, len(encrypted)):
    decrypt.append(ord(encrypted[i]) - key)
    #decrypt[i] = decrypt[i] - key
for i in range(0, len(decrypt)):
    decrypt[i] = chr(decrypt[i])

decrypted = open("decrypted.txt", "w")
for i in range(0, len(decrypt)):
    decrypted.write(decrypt[i])
decrypted.close()
print(decrypt)


