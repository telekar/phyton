# find MD5 hashes which, in hexadecimal, start with at least five zeroes. 
# The input to the MD5 hash is some secret key (your puzzle input, given below)
# followed by a number in decimal.

# Now find one that starts with six zeroes.

import hashlib

with open ( "puzzle4.txt","r") as f:
    puzzle = f.read()

def create_md5_hash(data):
    if isinstance(data, str):
      data = data.encode('utf-8')

    md5 = hashlib.md5()
    md5.update(data)
    return md5.hexdigest()

check5 = check6 =True
i = 0

while check5 or check6:
    #change i in str
    strI = str(i)

    hash_wert = create_md5_hash(puzzle+strI)

    if check5 and hash_wert[:5] == "00000":
        print('Part 1:',i)
        print(hash_wert)
        print()
        check5 = False

    if check6 and hash_wert[:6] == "000000":
        print('Part 2:',i)
        print(hash_wert)
        check6 = False
    
    i = i + 1

