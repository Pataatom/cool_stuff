from cryptography.fernet import Fernet
with open("kezz.key", "rb") as f:
    key = f.read()

file = Fernet(key)
with open("just_testing.txt", "rb") as original_file:
    original = original_file.read()

encrypted = file.encrypt(original)
with open("enc_Just.txt", "wb") as f:
    f.write(encrypted)