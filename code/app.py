import os
import time
import aes
import rsa

print('Press 1 for encryption smth and 2 for decryption')

way = input() 

if way == '1':

    print('Enter the file-name of text to be encrypted')

    input_path = os.path.abspath(input())

    print('Enter the file-name of the key')

    key_path = os.path.abspath(input())

    print('Encryption of text in progress.....')

    with open(input_path, 'rb') as f:
        data = f.read()

    with open(key_path, 'r') as f:
        key = f.read() 

    crypted_data = []
    crypted_key = []
    temp_data = []
    temp_key = []

    for byte in data:
        temp_data.append(byte)
    
    for byte in key:
        temp_key.append(byte)

    crypted_part = aes.encrypt(temp_data, temp_key)
    crypted_data.extend(crypted_part)

    out_path = os.path.join(os.path.dirname(input_path) , 'encrypted-' + os.path.basename(input_path))

    with open(out_path, 'xb') as ff:
        ff.write(bytes(crypted_data))
    
    print('Text file is encrypted Sucessfully')
    
    rsa.chooseKeys()

    file_option = input('Enter the file name of public key to encrypt main key')
    
    print('Encryption of key in progress.....')
    print('Please wait it may take several minutes.....')    
    message = "".join(temp_key)
    encrypted_key = rsa.encrypt(message, file_option)
    f_public = open('encrypted-key.txt', 'w')
    f_public.write(str(encrypted_key))
    f_public.close()

    print('Encryption is Done!!')

else:

    print('Enter the file name of encrypted key')

    d_key_path = os.path.abspath(input())

    with open(d_key_path, 'r') as f:
        d_key = f.read()

    print('Key Decryption in progess.....')
    print('Please wait it may take several minutes.....')

    d_message = rsa.decrypt(d_key)

    print('Enter the file name of encrypted text')

    d_input_path = os.path.abspath(input())

    with open(d_input_path, 'rb') as f:
        d_data = f.read()

    decrypted_data = []
    temp = []
    for byte in d_data:
        temp.append(byte)

    decrypted_part = aes.decrypt(temp, d_message)
    decrypted_data.extend(decrypted_part) 

    out_path = os.path.join(os.path.dirname(d_input_path) , 'decrypted_' + os.path.basename(d_input_path))

    with open(out_path, 'xb') as ff:
        ff.write(bytes(decrypted_data))

    print('File is Successfully Decrypted.')
    print()
    print('ACHIEVED HYBRID CRYPTOGRAPHY SUCCESSFULLY')