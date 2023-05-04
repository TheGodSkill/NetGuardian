import hashlib

target_hash = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8' # SHA-256 hash of 'password'


with open('rockyou.txt', 'r', encoding='latin-1') as f:
 passwords = f.read().splitlines()


for password in passwords:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if hashed_password == target_hash:
        print('Password cracked:', password)
        break
