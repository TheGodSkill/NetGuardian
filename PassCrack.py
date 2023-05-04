import hashlib

target_hash = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8' # SHA-256 hash of 'password'

# List of potential passwords
# you can use a list if you want
passwords = ['password', '123456', 'qwerty', 'letmein', 'admin']

# Loop through each password and hash it for comparison
for password in passwords:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if hashed_password == target_hash:
        print('Password cracked:', password)
        break
