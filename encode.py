string = input("输入要加密的字符串：")
key = int(input("输入秘钥："))

def encode_string(string, key):
    result = ""
    for c in string:
        result += chr(ord(c) + key)
    return result

print(encode_string(string, key))
