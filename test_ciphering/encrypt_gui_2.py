#Whitman spitzer - 11/18/2020
#first attempt at a gui for the encryption

import secrets
import PySimpleGUI as sg 
import os.path

sg.theme('DarkTeal1') #I thought this one was cool

#encoded_file = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\encoded_1.txt"  
#cipher_pad = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\cipher_pad_1.txt" 
#message_to_encode = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\message_1.txt"  

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

def encode_message(message_path, pad_path, encoded_path, encoded_name):        
    #cipher_pad = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\cipher_pad_{}.txt"  #need a way to automate these paths
    #cipher_pad = cipher_pad.format(pad_count)
    #encoded_file = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\encoded_1.txt"  
    
    pad_num_list = []
    ciphertext_list = []
    pre_msg_string = ''
    post_msg_string = ''
    full_msg_string = ''
    remaining_chars = 992
    
    encoded_path += "/" + encoded_name

    with open(pad_path, 'r') as pad:
        pad_list = pad.read()
    
    pad_list = pad_list.split(' ')    
    
    for x in pad_list:
        if x.isdigit():
            pad_num_list.append(int(x))
    
    with open(message_path, 'r') as msg_input:
        raw_msg_string = msg_input.read()

    split_index = secrets.randbelow(remaining_chars - len(raw_msg_string)) #generate a point somewhere between message length and 996, (996 for the delimiters |#)
    
    while len(pre_msg_string) < split_index:
        pre_msg_string += random_char()
    
    while len(post_msg_string) < (remaining_chars - split_index):
        post_msg_string += random_char()

    full_msg_string = pre_msg_string + "####" + raw_msg_string + "####" + post_msg_string
    
    for x in range(1000):
        ciphertext_list.append(ord(full_msg_string[x]) ^ pad_num_list[x]) # append character conversion of int converted ascii value of msg string index XOR bitwise operated w pad num list index
       
    with open(encoded_path, 'w') as encoded_msg:
        for x in range(1000):
            encoded_msg.write('%d' % ciphertext_list[x])
            encoded_msg.write(' ')
    return ciphertext_list

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

def save_txt_file(name, output, path):
    if not name:
        name = "generic_name.txt"
    
    path += '/' + name
    print(path)
    length = len(output)

    with open(path, 'w') as txt_file:
        for x in range(length):
            txt_file.write(output[x])
    
    return True

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
        sg.In(size=(23, 1), enable_events=True, key="-MESSAGE_FILE-"),
        sg.FileBrowse(),
    ],
]

pad_column_middle = [
    [
        sg.Text("One-Time Pad File (.txt files)"),
    ],
    [
        sg.In(size=(23,1), enable_events=True, key="-PAD_FILE-"),
        sg.FileBrowse(),
    ],
    [
        sg.Button("Generate One Time Pad(s)")
    ]
]

output_column_right = [
    [
        sg.Text("Output:"),
    ],
    [ 
        sg.Button('DECODE MESSAGE (if encoded input)'),
    ],
    [
        sg.Button('ENCODE MESSAGE (if decoded input)'),
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

window_1 = sg.Window("10BULLS10", layout) #main window

window_2_active = False #Pad generation window
window_3_active = False #decoded output window
window_4_active = False #encoded file save window

#Event Loop
while True:
    
    event_1, values_1 = window_1.read()
    
    if event_1 == "Exit" or event_1 == sg.WIN_CLOSED:
        break
    
    if event_1 == "-MESSAGE_FILE-":        
            message_file = values_1["-MESSAGE_FILE-"]

    elif event_1 == "-PAD_FILE-":
            pad_file = values_1["-PAD_FILE-"]
    
    elif not window_2_active and event_1 == "Generate One Time Pad(s)":
        window_2_active = True
     
        layout_2 = [
            [
                sg.Text("NOTE: NOT SECURE, USES secrets LIBRARY"),
            ],
            [
                sg.Text("Please Choose the folder in which to save Pad(s):"),
            ],
            [    
                sg.In(size=(23, 1), enable_events=True, key="-GENERATE_PAD_PATH-"),
                sg.FolderBrowse(),
            ],
            [
                sg.Text("Number of pad(s) you wish to generate (1-100):")
            ],
            [
                sg.In(size=(23, 1), enable_events=True, key="-PAD_NUM-"),
                sg.Button("Generate Pads")
            ],
        ]
        window_2 = sg.Window('10BULLS10 - TESTING ONLY', layout_2)
    
    if window_2_active:        
        event_2, values_2 = window_2.read()
    
        if event_2 == sg.WIN_CLOSED or event_2 == 'Exit':
            window_2_active = False
            window_2.close()

    elif not window_3_active and event_1 == "DECODE MESSAGE (if encoded input)":
        window_3_active = True
        decoded_output = "AN ERROR OCCURRED" #if this isn't modified, something broke
        
        try:
            if message_file and pad_file:
                decoded_output = decode_message(message_file, pad_file)
        except:
            pass

        layout_3 = [
            [
                sg.Text("The decoded message is:")
            ],
            [
                sg.Multiline(decoded_output, key='-XOR_RESULT_MULTILINE-'),
            ],
            [
                sg.Text("Please enter a name [name.txt] for your file:")
            ],
            [
                sg.In(size=(42, 1), enable_events=True, key="-DECODED_FILE_NAME-"),
            ],
            [
                sg.Text("Please select a folder and hit save.")
            ],
            [
                sg.In(size=(28, 1), enable_events=True, key="-DECODED_OUTPUT_PATH-"),
                sg.FolderBrowse("Select Folder"),
                sg.Button("Save", key="-SAVE_DECODED_MESSAGE-"),
            ],
        ]

        window_3 = sg.Window('10BULLS10', layout_3)

    while window_3_active:        
        event_3, values_3 = window_3.read()
    
        if event_3 == sg.WIN_CLOSED or event_3 == 'Exit':
            window_3_active = False
            window_3.close()

        if event_3 == "-DECODED_FILE_NAME-":
            decoded_file_name = values_3["-DECODED_FILE_NAME-"]
        
        if event_3 == "-SAVE_DECODED_MESSAGE-":
            if not decoded_file_name:
                sg.popup("Please enter a name for the file")
            
            decoded_file_path = values_3["-DECODED_OUTPUT_PATH-"]
            save_txt_file(decoded_file_name, decoded_output, decoded_file_path)
            window_3_active = False
            window_3.close()
    
    if not window_4_active and event_1 == "ENCODE MESSAGE (if decoded input)":
        window_4_active = True
        Xor_output = "AN ERROR OCCURRED" #if this isn't modified, something broke

        layout_4 = [
            [
                sg.Text("Please enter a name for your encoded file [name.txt]:")
            ],
            [
                sg.In(size=(34, 1), enable_events=True, key="-ENCODED_OUTPUT_NAME-"),
            ],
            [
                sg.Text("Please select a folder in which to save the encoded message:")
            ],
            [
                sg.In(size=(34, 1), enable_events=True, key="-ENCODED_OUTPUT_PATH-"),
                sg.FolderBrowse("Select Folder to Save"),
                sg.Button("Save", key="-ENCODED_SAVE-")
            ],
        ]

        window_4 = sg.Window('10BULLS10', layout_4)    
    
    while window_4_active:        
        event_4, values_4 = window_4.read()
    
        if event_4 == sg.WIN_CLOSED or event_4 == 'Exit':
            window_4_active = False
            window_4.close()

        elif event_4 == "-ENCODED_OUTPUT_NAME-":
            name_for_encoded_file = values_4["-ENCODED_OUTPUT_NAME-"]

        elif event_4 == "-ENCODED_SAVE-":
                encoded_path = values_4["-ENCODED_OUTPUT_PATH-"]
                Xor_output = encode_message(message_file, pad_file, encoded_path, name_for_encoded_file)
                sg.popup_scrolled(Xor_output, title="ENCODED MESSAGE",)
                window_4_active = False
                window_4.close()

    if event_1 == "Feature Test":
        sg.popup_scrolled("what")

window_1.close()

