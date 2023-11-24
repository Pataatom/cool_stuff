from cryptography.fernet import Fernet
with open("kezz.key", "rb") as f:
    key = f.read()

file = Fernet(key)
with open("enc_Just.txt", "rb") as encrypted_file:
    encrypted = encrypted_file.read()

norm = file.decrypt(encrypted)
with open("dec_Just.txt", "wb") as fi:
    fi.write(norm)
