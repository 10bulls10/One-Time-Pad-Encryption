#whitman spitzer - 11/16/2020
#this program accesses an encoded file and a pad to provide a message



encoded_file = "C:\\Users\\whits\\STUFF\\Dumpster\\projects\\vernam_1\\test_ciphering\\encoded_1.txt"  
cipher_pad = "C:\\Users\\whits\\STUFF\\Dumpster\\projects\\vernam_1\\test_ciphering\\cipher_pad_1.txt" 
decoded_nums = []
pad_num_list = []
encoded_num_list = []
decoded_msg = ' '

with open(cipher_pad, 'r') as pad:
    pad_strlist = pad.read()

pad_strlist = pad_strlist.split(' ')

with open(encoded_file, 'r') as encoded_msg:
    encoded_strlist = encoded_msg.read()

encoded_strlist = encoded_strlist.split(' ')

for x in pad_strlist:
    if x.isdigit():
        pad_num_list.append(int(x))

for x in encoded_strlist:
    if x.isdigit():
        encoded_num_list.append(int(x))

for x in range(1000):
    decoded_nums.append(encoded_num_list[x] ^ pad_num_list[x]) #repeat bitwise XOR operation between ciphertext and pad to produce decoded ascii vals

for x in decoded_nums: #convert decoded ascii vals into chars
    decoded_msg += chr(x)

separated_msg_list = decoded_msg.rsplit("####")

print(separated_msg_list[1]) #since the delimiters are unique (7.4 million to one), the separated list should have 3 elements, before delimiter, msg, and after delimiter. therefore msg is index 1