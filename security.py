from cryptography.fernet import Fernet

# This creates your encryption key
# In real app, you keep this secret

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_data(data):
    # This encrypts private keys
    return cipher.encrypt(data.encode())

def generate_2fa_code():
    # We will connect this to Google Authenticator later 
    import pyotp
    secret = pyotp.random_base32()
    return secret