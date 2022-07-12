print("编辑代码3,4两行，以开始解密")

s = ""
key = 0

def decode_string(s, key):
    r = ""
    for c in s:
        r += chr(ord(c) - key)
    return r

print(decode_string(s, key))
