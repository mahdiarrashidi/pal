# pal
Profit and Loss WebApp_python

# Encrypted Credentials Generation

1. Run the Python script to generate encryption key file (`key.key`) and credential.env file.

    ```
    python3 
    ```

2. The code.

    ```python
    from cryptography.fernet import Fernet
    import os
    def generate_key():
    return Fernet.generate_key()

    def encrypt_password(password, key):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(password.encode())
    return cipher_text

    # Generate a new key and save it in a file
    key = generate_key()
    with open('key.key', 'wb') as key_file:
    key_file.write(key)

    # Create the encrypted password
    password = "123"
    encrypted_password = encrypt_password(password, key)

    # put the info in a .env file
    with open('credential.env', 'w') as env_file:
    env_file.write(f"DB_PASSWORD={encrypted_password.decode()}")

    ```

3. Update the credential.env file:
4. ```
    DB_HOST=localhost
    DB_USER=admin
    DB_PASSWORD=gAAAAABleZffY-r0BKYoNwmilb0_lj1Um3hSZVDs5lNWg_w-sDvGQriaTnA580azOwSxHUYZL1oq-Ps3a69_DoLH3cylYrzBaA==
    DB_NAME=pal_db1
   ```
