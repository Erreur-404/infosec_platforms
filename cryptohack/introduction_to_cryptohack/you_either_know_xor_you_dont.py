encrypted = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

key = list()
key.append(ord('c') ^ encrypted[0])
key.append(ord('r') ^ encrypted[1])
key.append(ord('y') ^ encrypted[2])
key.append(ord('p') ^ encrypted[3])
key.append(ord('t') ^ encrypted[4])
key.append(ord('o') ^ encrypted[5])
key.append(ord('{') ^ encrypted[6])
# Lets you see the key that you have for now
# print("".join([chr(i) for i in key]))
key.append(ord('y'))


decrypted = "".join([chr(encrypted[i] ^ key[i % len(key)]) for i in range(len(encrypted))])
print(f'Decrypted: {decrypted}')