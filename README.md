# pal
Profit and Loss WebApp_python


## To create the Encrypted credentials:
'python3'
#from cryptography.fernet import Fernet
#import os

>>> def generate_key():
        return Fernet.generate_key()

>>> def encrypt_password(password, key):
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(password.encode())
        return cipher_text

 ##Generate a new key and save it in a file
#key = generate_key()
#with open('key.key', 'wb') as key_file:
        key_file.write(key)

    #Create the encrypted password
>>> password = "123"
>>> encrypted_password = encrypt_password(password, key)

    #Put the info in a .env file
>>> with open('credential.env', 'w') as env_file:
        env_file.write(f"DB_PASSWORD={encrypted_password.decode()}")




The files are generated. Now edit the credential.env as follow:

DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=gAAAAABleZffY-r0BKYoNwmilb0_lj1Um3hSZVDs5lNWg_w-sDvGQriaTnA580azOwSxHUYZL1oq-Ps3a69_DoLH3cylYrzBaA==
DB_NAME=pal_db1
