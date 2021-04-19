import os
import time
import aes
import rsa
import cloudinary
import cloudinary.uploader
from flask import Flask,render_template,request,url_for,session

cloudinary.config( 
  cloud_name = "securefilestoragecloud", 
  api_key = "671392448133668", 
  api_secret = "47cweUn3dXjEpBEhVpsrYy9MHj8" 
)
app = Flask(__name__)
app.secret_key = '5791628bb0b13ce0c676dfde28jbsdb'

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/encrypt',methods=[ 'GET','POST'])
def encrypt():
    return render_template('encrypt1.html', title = 'Encrypt')


@app.route('/encrypt1',methods=['GET','POST'])
def encrypt_text():
   plainfile=(request.files['plainfile']).filename
   keyfile=(request.files['key']).filename
   input_path = os.path.abspath(plainfile)
   print(input_path)
   key_path = os.path.abspath(keyfile)

   print('Encryption of text in progress.....')

   with open(input_path, 'rb') as f:
        data = f.read()

   with open(key_path, 'r') as f:
        key = f.read() 

   crypted_data = []
#    crypted_key = []
   temp_data = []
   temp_key = []

   for byte in data:
        temp_data.append(byte)
    
   for byte in key:
        temp_key.append(byte)
   session["temp_key"]=temp_key
   crypted_part = aes.encrypt(temp_data, temp_key)
   crypted_data.extend(crypted_part)

   out_path = os.path.join(os.path.dirname(input_path) , 'encrypted-' + os.path.basename(input_path))

   with open(out_path, 'xb') as ff:
        ff.write(bytes(crypted_data))

   with open(ff.name, 'rb') as file:
        response= cloudinary.uploader.upload(file,resource_type = "raw", use_filename ='true')
<<<<<<< HEAD
   session['response']=response['secure_url']

   rsa.chooseKeys()
   return render_template('encrypt2.html', title = 'encrypt2')
   
@app.route('/encrypt2',methods=['GET','POST'])
def encryptkey():
     # rsa.chooseKeys()
     file_option=(request.files['publickey']).filename   
     message = "".join(session['temp_key'])
     encrypted_key = rsa.encrypt(message, file_option)
     f_public = open('encrypted-key.txt', 'w')
     f_public.write(str(encrypted_key))
     f_public.close()

     return render_template('enc_success.html',response=session['response'])




@app.route('/decrypt',methods=[ 'GET','POST'])
def decrypt():
    return render_template('decrypt1.html', title = 'Decrypt')

@app.route('/decrypt1',methods=['GET','POST'])
def decrypt_key():
    dec_key = (request.files['enckey']).filename
    d_key_path = os.path.abspath(dec_key)
=======

    print('Text file is encrypted successfully.')
    
    
    rsa.chooseKeys()

    file_option = input('Enter the file name of public key to encrypt main key')
    
    print('Encryption of key in progress.....')
    print('Please wait it may take several minutes.....')    
    message = "".join(temp_key)
    encrypted_key = rsa.encrypt(message, file_option)
    f_public = open('encrypted-key.txt', 'w')
    f_public.write(str(encrypted_key))
    f_public.close()

    print('Encryption is Done!! File uploaded to cloud.')
    print(response['secure_url'])

else:

    print('Enter the file name of encrypted key')

    d_key_path = os.path.abspath(input())

>>>>>>> d79bbae800c861846934a2561ea4bae7ed935932
    with open(d_key_path, 'r') as f:
        d_key = f.read()

    print('Key Decryption in progess.....')
    print('Please wait it may take several minutes.....')

    d_message = rsa.decrypt(d_key)
    session['d_message']=d_message
    return render_template('decrypt2.html', title = 'decrypt2')

#     print('Enter the file name of encrypted text')
@app.route('/decrypt2',methods=['GET','POST'])
def decrypt_text():
    dec_input = (request.files['enctext']).filename
    d_input_path = os.path.abspath(dec_input)

    with open(d_input_path, 'rb') as f:
        d_data = f.read()

    decrypted_data = []
    temp = []
    for byte in d_data:
        temp.append(byte)

    decrypted_part = aes.decrypt(temp, session['d_message'])
    decrypted_data.extend(decrypted_part) 

    out_path = os.path.join(os.path.dirname(d_input_path) , 'decrypted_' + os.path.basename(d_input_path))

    with open(out_path, 'xb') as ff:
        ff.write(bytes(decrypted_data))
    return render_template('dec_success.html', title = 'dsuccess')
#     print('File is Successfully Decrypted.')
#     print()
#     print('ACHIEVED HYBRID CRYPTOGRAPHY SUCCESSFULLY')


<<<<<<< HEAD
if __name__ == '__main__':
    app.debug=True
    app.run()
=======
    print('File is Successfully Decrypted.')
    print()
    print('ACHIEVED HYBRID CRYPTOGRAPHY SUCCESSFULLY')
>>>>>>> d79bbae800c861846934a2561ea4bae7ed935932
