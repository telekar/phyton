# Solved with help by youtube

with open ( "puzzle7.txt","r") as f:
    inputstr = f.read()

for n in range(len(inputstr)):
    inputList = inputstr.split("\n")

table = {}

for line in inputList:
    left , right =line.split(" -> ")
    table [right] = left

mem = {}

def get_val(var):
    if var.isdigit():
        return int(var)
    if var in mem:
        return mem[var]
    s = table[var]
    if s.isdigit():
        mem[var] = int(s)
        return mem[var]
    if s.startswith("NOT"):
        s1 = get_val(s[4:])
        t = bin(s1)[2:].zfill(16)                           #wandelt string in eine 16bit binärzahl ohne 'ob'
        t = ''.join('1' if c == '0' else '0' for c in t)    #negiert bitweise und erstellt einen string
        result = int('0b' + t, 2)                           #wandelt neuen string in zahl
        mem[var] = result
        return mem[var]
    if 'OR' in s:
        s1 ,s2 = s.split(' OR ')
        mem[var] = get_val(s1) | get_val(s2)
        return mem[var]
    if 'AND' in s:
        s1 ,s2 = s.split(' AND ')
        mem[var] = get_val(s1) & get_val(s2)
        return mem[var]
    if 'LSHIFT' in s:
        s1, d =s.split(' LSHIFT ')
        mem[var] = get_val(s1) << int(d)
        return mem[var]
    if 'RSHIFT' in s:
        s1, d =s.split(' RSHIFT ')
        mem[var] = get_val(s1) >> int(d)
        return mem[var]
    mem[var] = get_val(s)
    return mem[var]

#part 1
print(get_val('a'))

#part 2
mem = {}
table['b'] = '16076'
print(get_val('a'))


