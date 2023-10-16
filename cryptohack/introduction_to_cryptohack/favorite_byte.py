encrypted = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

key = ord('c') ^ encrypted[0]

decrypted = "".join([chr(encrypted[i] ^ key) for i in range(len(encrypted))])
print(f'Decrypted: {decrypted}')