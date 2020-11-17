# S. Whitman Spitzer 11/16/2020
# this combines the message in a txt file with a pad, to create unreadable ciphertext

import secrets

message_to_encode = "C:\\Users\\whits\\STUFF\\Dumpster\\projects\\vernam_1\\test_ciphering\\message_1.txt"  

def random_char():
    
    return chr(secrets.randbelow(93) + 33)

def encode_message(message_path, pad_count):    
    
    cipher_pad = "C:\\Users\\whits\\STUFF\\Dumpster\\projects\\vernam_1\\test_ciphering\\cipher_pad_{}.txt"  #need a way to automate these paths
    cipher_pad = cipher_pad.format(pad_count)
    encoded_file = "C:\\Users\\whits\\STUFF\\Dumpster\\projects\\vernam_1\\test_ciphering\\encoded_1.txt"  
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


encode_message(message_to_encode, 1) #eventually indices on the pads will increment somehow, also need to overwrite prev pads

