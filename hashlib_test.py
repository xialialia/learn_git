import hashlib

m = hashlib.md5()  # m=hashlib.sha256()

m.update('hello'.encode('ascii'))

print(m.hexdigest()) #5d41402abc4b2a76b9719d911017c592