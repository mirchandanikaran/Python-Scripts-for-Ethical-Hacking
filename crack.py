import hashlib

flag = 0
counter = 0
pass_hash = input("Enter MD5 hash: ")
wordlist = input("File name: ")
try: 
    pass_file = open (wordlist, "r")
except:
    print("No file found")
    quit()


for word in pass_file:
    enc_wrd = word.encode('utf-8')
    
    # creating a hex digest, stripping white spaces
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    # comparing our input hash with all hashes we 
    # are producing from the words in the dictionary

    #print(word)
    #print(digest)
    #p rint(pass_hash)

    if digest == pass_hash:
        print("Password found")
        print("Password is " + word)
        print(counter)
        flag = 1
        break
    
if flag == 0:
    print("Password not in the wordlist")