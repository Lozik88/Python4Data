import string
letters = string.ascii_uppercase[0:]
# names = ["Jarrell","Amy","Roewan","Caesar","Eevee"]

def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]

def new_names(names):
    insert = []
    i=0
    for name in names:
        name = name[1:]
        for letter in letters:
            nm = letter+name
            i+=1
            #print(f"{i} {nm}")
            insert.append([i,nm])
    return insert
    