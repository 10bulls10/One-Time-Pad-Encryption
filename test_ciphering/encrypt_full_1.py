#Whitman spitzer - 11/18/2020
#this is the file that combines the pad generation and encode and decode prototypes in one program

import secrets
import PySimpleGUI as sg 
import os.path

encoded_file = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\encoded_1.txt"  
cipher_pad = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\cipher_pad_1.txt" 
message_to_encode = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\message_1.txt"  

def generate_pad(filename):
    
    number_list1 = []
    
    for x in range(1000):
        number_list1.append(secrets.randbelow(93))

    with open(filename, 'w') as cipher_output:
        for x in range(1000):
            cipher_output.write('%d' % number_list1[x])
            cipher_output.write(' ')
        
def random_char():
    
    return chr(secrets.randbelow(93) + 33)

def encode_message(message_path, pad_count):    
    
    cipher_pad = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\cipher_pad_{}.txt"  #need a way to automate these paths
    cipher_pad = cipher_pad.format(pad_count)
    encoded_file = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\encoded_1.txt"  
    pad_num_list = []
    ciphertext_list = []
    pre_msg_string = ''
    post_msg_string = ''
    full_msg_string = ''
    remaining_chars = 992

    with open(cipher_pad, 'r') as pad:
        pad_list = pad.read()
    
    pad_list = pad_list.split(' ')    
    
    for x in pad_list:
        if x.isdigit():
            pad_num_list.append(int(x))
    
    with open(message_path, 'r') as msg_input:
        raw_msg_string = msg_input.read()

    split_index = secrets.randbelow(remaining_chars - len(raw_msg_string)) #generate a point somewhere between message length and 996, (996 for the delimiters |#)
    #print(split_index)
    
    while len(pre_msg_string) < split_index:
        pre_msg_string += random_char()
    
    while len(post_msg_string) < (remaining_chars - split_index):
        post_msg_string += random_char()

    full_msg_string = pre_msg_string + "####" + raw_msg_string + "####" + post_msg_string
    
    for x in range(1000):
        ciphertext_list.append(ord(full_msg_string[x]) ^ pad_num_list[x]) # append character conversion of int converted ascii value of msg string index XOR bitwise operated w pad num list index
       
    with open(encoded_file, 'w') as encoded_msg:
        for x in range(1000):
            encoded_msg.write('%d' % ciphertext_list[x])
            encoded_msg.write(' ')
    print("  MESSAGE ENCODED ")

def decode_message(encoded_file, cipher_pad):

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
    return separated_msg_list[1]


#########################################################################      

generate_pad(cipher_pad)

encode_message(message_to_encode, 1) #eventually indices on the pads will increment somehow, also need to overwrite prev pads

print(decode_message(encoded_file, cipher_pad)) #since the delimiters are unique (7.4 million to one), the separated list should have 3 elements, before delimiter, msg, and after delimiter. therefore msg is index 1