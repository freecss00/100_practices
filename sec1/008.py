
def cipher(s, decryption=False):
    return ''.join([chr(219 - ord(c)) if 'a' <= c <= 'z' else c for c in s])


plain = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
encrypted = cipher(plain)
decrypted = cipher(encrypted)
print(plain)
print(encrypted)
print(decrypted)
