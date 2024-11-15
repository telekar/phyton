import hashlib

with open ( "puzzle_4a.txt","r") as f:
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
        print(i)
        print(hash_wert)
        check5 = False

    if check6 and hash_wert[:6] == "000000":
        print(i)
        print(hash_wert)
        check6 = False
    
    i = i + 1

