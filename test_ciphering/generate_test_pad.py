#S. whitman spitzer - 11/16/2020
# Attempt to generate numbers in a .txt file to use as a test pad

import secrets

filename = "C:\\Users\\whits\\STUFF\\Local_Env\\projects\\vernam_1\\Pythonense\\test_ciphering\\cipher_pad_1.txt"  

def generate_pad(filename):
    
    number_list1 = []
    
    for x in range(1000):
        number_list1.append(secrets.randbelow(93))

    with open(filename, 'w') as cipher_output:
        for x in range(1000):
            cipher_output.write('%d' % number_list1[x])
            cipher_output.write(' ')
        
generate_pad(filename)














