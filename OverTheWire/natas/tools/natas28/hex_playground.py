import base64

def decode():
    test_string = '''
G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPJULNYyXxAAoutn165diNcRSHmaB7HSm1mCAVyTVcLgDq3tm9uspqc7cbNaAQ0sTFc=
'''
    test_list = test_string.split('\n')
    with open('natas28/info.txt', 'a') as f:    
        for line in test_list:
            test_bytes = line.encode()
            print(len(base64.b64decode(test_bytes)))
            f.write(str(base64.b64decode(test_bytes)) + ' size = ' + str(len(base64.b64decode(test_bytes))) + '\n')


def xor(string1, string2):
    result = ""
    for a, b in zip(string1, string2):
        result += chr(ord(a) ^ ord(b))
    return result.encode()


if __name__ == "__main__":
    # decode()
    key = xor("G\xb7\xca\x91U\xee\xfb\xcb<\x90\x96Nt\xb5\x90|", '\x15\xb1\xf8\xa3l\xdb\xc4\xc6\xd3\xca\xcb_6\xe5\xa0\xba')
    print(key.decode())
    # print(ord(result.decode()))
    # print(xor(key.decode(), '\x93>`\xcc\xd1\x84x1\xce~\xb9c\x84\x0f\xa4B').decode())