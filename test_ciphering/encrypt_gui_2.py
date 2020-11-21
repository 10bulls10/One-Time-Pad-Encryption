#Whitman spitzer - 11/18/2020
#first attempt at a gui for the encryption

import secrets
import PySimpleGUI as sg 
import os.path

sg.theme('DarkTeal1') #I thought this one was cool

#encoded_file = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\encoded_1.txt"  
#cipher_pad = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\cipher_pad_1.txt" 
#message_to_encode = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\message_1.txt"  

def generate_pad(path, count_str): #since it's from the gui input, count comes in as a string
    
    count = int(count_str)
    path += "/cipher_pad_"
    
    for q in range(count):
        number_list1 = []

        for x in range(1000):
            number_list1.append(secrets.randbelow(93))

        count_exten = "{}.txt"
        count_exten = count_exten.format(q + 1)
        print("iter")
        curr_path = path + count_exten
        
        with open(curr_path, 'w') as cipher_output:
            for x in range(1000):
                cipher_output.write('%d' % number_list1[x])
                cipher_output.write(' ')
        
def kill_pad(path):
    number_list = []
    print("destroy pad")

    for x in range(1000):
            number_list.append(secrets.randbelow(93))
    
    with open(path, 'w+') as cipher_output:
            for x in range(1000):
                cipher_output.write('%d' % number_list[x])
                cipher_output.write(' ')        
    return 1
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
    [
        sg.Checkbox("Automatically overwrite pad after use", default=False, enable_events=True, key="-DESTROY_PAD_CHECK-")
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
        sg.Button('Exit'), sg.Button('Instructions'),
    ]
]

window_1 = sg.Window("10BULLS10", layout) #main window

window_2_active = False #Pad generation window
window_3_active = False #decoded output window
window_4_active = False #encoded file save window
destroy_pad = False

#Event Loop
while True:
    
    event_1, values_1 = window_1.read()
    
    if event_1 == "Exit" or event_1 == sg.WIN_CLOSED:
        break
    
    if event_1 == "-MESSAGE_FILE-":        
            message_file = values_1["-MESSAGE_FILE-"]

    elif event_1 == "-PAD_FILE-":
            pad_file = values_1["-PAD_FILE-"]
    
    if values_1["-DESTROY_PAD_CHECK-"]:
        print("here")
        destroy_pad = True

    else:
        print("not here")
        destroy_pad = False
    
    if not window_2_active and event_1 == "Generate One Time Pad(s)":
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
                sg.Button("Generate Pads", key="-GEN_PADS-")
            ],
        ]
        window_2 = sg.Window('10BULLS10 - TESTING ONLY', layout_2)
    
    new_pad_path = "ERROR"
    new_pad_num = 3.14 #number should be an int, (and in conversion would be floored, so if it reads 3.14 then its invalid)
    while window_2_active:        
        event_2, values_2 = window_2.read()
        
        if event_2 == sg.WIN_CLOSED or event_2 == 'Exit':
            window_2_active = False
            window_2.close()

        if event_2 == "-GENERATE_PAD_PATH-":
            new_pad_path = values_2["-GENERATE_PAD_PATH-"]
        
        if event_2 == "-PAD_NUM-":
            new_pad_num = values_2["-PAD_NUM-"]
        
        elif event_2 == "-GEN_PADS-":
            
            if new_pad_path == "ERROR" and new_pad_num == 3.14:
                sg.popup("Please choose a folder and number of pad(s) to generate.")
            
            else:
                generate_pad(new_pad_path, new_pad_num)
                window_2_active = False
                window_2.close()

    if not window_3_active and event_1 == "DECODE MESSAGE (if encoded input)":
        window_3_active = True
        decoded_output = "AN ERROR OCCURRED" #if this isn't modified, something broke
        
        try:
            if message_file and pad_file:
                decoded_output = decode_message(message_file, pad_file)
                print(pad_file)
                print(int(pad_file[-5]))

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

    if event_1 == "Instructions":
        sg.popup_scrolled("""
To decrypt a message: 
Select a message. You must know which pad was used to encrypt it.
Select that pad (should be numbered, such as cipher_pad_1.txt ) 
Hit the DECODE button, which will activate a popup window.
If you wish to save the decoded message, select a folder, choose a name, and hit Save.
To encrypt a message:
Select a message (plain english .txt file). 
Select a pad (the person decrypting it will need a copy)
Hit the ENCODE button. Choose a folder in which to save the encoded message and a name, and hit Save.
To generate pads: 
Hit the Generate One Time Pad(s) button.
Select a folder in which to save your pads. 
Select a number of pad(s) to generate (says 1-100 but can be any number, though huge numbers could cause you problems). The pads will appear in that folder, labeled cipher_pad_[number].txt.
IMPORTANT NOTES:
This software is in no way secure. AT ALL. 
The protocol used for generating pads is the Python Secrets library, which relies on your OS for randomness. IT IS NOT RANDOM ENOUGH.
This thing saves .txt files on your hard drive, if anything can read or track them, then the messages you send are not secure. If pads are not destroyed, messages are not secure, if pads are used more then once pads are not secure. As of November 2020, nothing about this program should be considered secure.""", title="Instructions")

window_1.close()

