def encode(m):
    L = []
    for x in m:
        num = ord(x)
        L.append(num)
    return L
def decode(l):
    string = ""
    for x in l:
        char = chr(x)
        string += char
    return string
'''
m = input()
l = encode(m)
s = decode(l)
print(l)
print(s)
'''