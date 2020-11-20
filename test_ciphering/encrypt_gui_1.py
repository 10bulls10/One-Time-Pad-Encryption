#Whitman spitzer - 11/18/2020
#first attempt at a gui for the encryption

import secrets
import PySimpleGUI as sg 
import os.path

sg.theme('BlueMono') #I thought this one was cool

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

def encode_message(message_path, pad_path):    
    
    #cipher_pad = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\cipher_pad_{}.txt"  #need a way to automate these paths
    #cipher_pad = cipher_pad.format(pad_count)
    encoded_file = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\encoded_1.txt"  
    pad_num_list = []
    ciphertext_list = []
    pre_msg_string = ''
    post_msg_string = ''
    full_msg_string = ''
    remaining_chars = 992

    with open(pad_path, 'r') as pad:
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

#generate_pad(cipher_pad)

#encode_message(message_to_encode, cipher_pad) #eventually indices on the pads will increment somehow, also need to overwrite prev pads

#print(decode_message(encoded_file, cipher_pad)) #since the delimiters are unique (7.4 million to one), 
# the separated list should have 3 elements, before delimiter, msg, and after delimiter. therefore msg is index 1

#########################################################################

message_column_left = [
    [
        sg.Text("Input File (Encoded/Decoded .txt file)"),
    ],
    [
        sg.In(size=(23, 1), enable_events=True, key="-MESSAGE_FOLDER-"),
        sg.FileBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(30, 10), key="-MESSAGE_FILE LIST-"
        )
    ],
]

pad_column_middle = [
    [
        sg.Text("One-Time Pad File (.txt files)"),
    ],
    [
        sg.In(size=(23,1), enable_events=True, key="-PAD_FOLDER-"),
        sg.FileBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(30, 10), key="-PAD_FILE LIST-"
        )
    ],
]

output_column_right = [
    [
        sg.Text("Output (decoded msg if encoded input and vice versa)"),
    ],
    [ 
        sg.Button('CONDUCT XOR OPERATIONS'),
    ],
    [
        sg.Multiline(key='-XOR_RESULT-', size=(30, 1)),
    ],
]

layout = [
    [
        sg.Column(message_column_left), 
        sg.VSeparator(), 
        sg.Column(pad_column_middle), 
        sg.VSeparator(), 
        sg.Column(output_column_right),
    ],
    [
        sg.Button('Exit'), sg.Button('Feature Test'),
    ]
]

window = sg.Window("10BULLS10", layout)

#Event Loop
while True:
    
    event, values = window.read()
    
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if event == "-MESSAGE_FOLDER-":
        message_folder = values["-MESSAGE_FOLDER-"]
        try:
            message_files_list = os.listdir(message_folder)
        except:
            message_files_list = []

        msgfnames = [
            f
            for f in message_files_list
            if os.path.isfile(os.path.join(message_folder, f))
            and f.lower().endswith((".txt"))
        ]
        
        window["-MESSAGE_FILE LIST-"].update(msgfnames)
    
    elif event == "-MESSAGE_FILE LIST-":
        try:
            msgfilename = os.path.join(
                values["-MESSAGE_FOLDER-"], values["-MESSAGE_FILE LIST-"][0]
            )
        except:
            pass

    elif event == "-PAD_FOLDER-":
        pad_folder = values["-PAD_FOLDER-"]
        try:
            pad_files_list = os.listdir(pad_folder)
        except:
            pad_folder_list = []
        
        padfnames = [
            f 
            for f in pad_files_list
            if os.path.isfile(os.path.join(pad_folder, f))
            and f.lower().endswith((".txt"))
        ]
        window["-PAD_FILE LIST-"].update(padfnames)
    elif event == "Feature Test":
        sg.popup_scrolled("what")

window.close()

