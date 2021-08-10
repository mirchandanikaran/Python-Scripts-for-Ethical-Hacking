# Program to hash text

import hashlib as hl

hashValue = input("Enter a string to hash: ")

hobj1 = hl.md5()
hobj1.update(hashValue.encode())
print("MD5: " + hobj1.hexdigest())



hobj2 = hl.sha1()
hobj2.update(hashValue.encode())
print("SHA-1: " + hobj2.hexdigest())


hobj3 = hl.sha224()
hobj3.update(hashValue.encode())
print("SHA-224: " + hobj3.hexdigest())


hobj4 = hl.sha256()
hobj4.update(hashValue.encode())
print("SHA-256: " + hobj4.hexdigest())


hobj5 = hl.sha512()
hobj5.update(hashValue.encode())
print("SHA-512: " + hobj5.hexdigest())