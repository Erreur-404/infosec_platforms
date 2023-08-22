import urllib.request as url
import urllib.parse
import string
import subprocess

NATAS_URL = 'http://natas28.natas.labs.overthewire.org/search.php'
NATAS_USERNAME = 'natas28'
NATAS_PWD = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'


def initialPageConnexion():
    '''
    Connects to the page with the given credentials. This function
    has to be called before trying anything on the webpage.
    '''
    auth_handler = url.HTTPBasicAuthHandler()
    auth_handler.add_password(
        'Authentication required', NATAS_URL, NATAS_USERNAME, NATAS_PWD)

    opener = url.build_opener(auth_handler)
    url.install_opener(opener)

    # This commented out tactic also works. The website accepts the Authorization header
    # after having connected at least once

    # request = url.Request(NATAS_URL)
    # request.add_header('Authorization', 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==')
    # output = url.urlopen(request)

    output = url.urlopen(NATAS_URL)

    # This part is not necessary. It was only to prove myself that the urllib package works
    # with open('output.html', 'w') as file:
    #     file.write(output.read().decode())


def correspondingQuery(string):
    '''
    Determines if the string is the correct id or not

        Parameters:
            string : The id

        Returns:
            True if the id is correct. False otherwise
    '''
    request = urllib.parse.urlencode({'query': string})
    request = request.encode('ascii')

    post_request = url.Request(NATAS_URL, request)

    output = url.urlopen(post_request)
    output = output.read().decode()

    if (output.find("Incorrect amount of PKCS#7 padding for blocksize") != -1):
        return "No"
    elif (output.find("Invalid PKCS#7 padding encountered") != -1):
        return "Invalid"
    elif (output.find("Zero padding found instead of PKCS#7 padding") != -1):
        return "Correct padding!"
    elif (output.find("Whack Computer Joke Database")):
        return "Whack Computer Joke Database"
    else:
        return "Awkward, need further investigation"


def base64_equivalent_query(number):
    # if (number < 16):
    #     number = hex(number)
    #     number = f'0{number[2:]}'
    # else:
    #     number = hex(number)
    #     number = f'{number[2:]}'
    return subprocess.check_output(['natas28/tob64.sh', number]).decode().strip()

# Originaux:     904f4b2abf2c2d76 86aa72a53151c970
# Modifiés:      7a2543eef4a34521 86aa72a53151c970


def decrypt(original_cipher, block_size):  # Block size is the number of bytes composing a block
    cipher_length = len(original_cipher) / 2
    if cipher_length % block_size != 0:
        return "Error: size of cipher is not a multiple of the block_size"

    ciphers = [original_cipher[n:n+block_size*2]
               for n in range(0, len(original_cipher), 16)]
    print(f'Ciphers are : {ciphers}')
    plain_text = ""
    for i in range(0, len(ciphers)-1):
        print(f'Decrypting {ciphers[i+1]}...')
        plain_text += decrypt_next_block(ciphers[i])
    return plain_text


# A partir d'ici, on utilise des listes
def decrypt_next_block(precedent_cipher):
    # Pour le test, ajuster à la valeur que j'ai utilisée ('7a2543eef4a34521')
    precedent_cipher = to_list(precedent_cipher)
    custom_cipher = ['aa'] * len(precedent_cipher)
    block_size = len(precedent_cipher)
    plaintext = bruteforce_plaintext(block_size, 1, [''] * block_size, custom_cipher, precedent_cipher)
    return plaintext


def to_list(block):
    return [block[i:i+2] for i in range(0, len(block), 2)]


def bruteforce_plaintext(k, padding, plaintext, forged_cipher, precedent_cipher):
    print(f'DEBUG : Entering bruteforce_plaintext with k = {k} and padding = {padding}')
    number_of_bytes = len(precedent_cipher)
    possible_enciphered_paddings = get_possible_enciphered_paddings(forged_cipher, padding)
    print(f'Possible enciphered paddings are {possible_enciphered_paddings}')
    for enciphered_padding in possible_enciphered_paddings:  # Separe les chemins
        plaintext[k] = compute_plaintext(padding, precedent_cipher[k], enciphered_padding)
        for i in range(number_of_bytes, k, -1):
            forged_cipher[i] = compute_forged_byte(padding, plaintext[i], precedent_cipher[i])
        if k == 1:
            return plaintext

        print(f'With enciphered_padding = {enciphered_padding}, plaintext = {plaintext} and forged_cipher = {forged_cipher}')

        result = bruteforce_plaintext(k-1, padding+1, plaintext, forged_cipher, precedent_cipher)
        if len(result) == number_of_bytes:
            return result
    return "Could not decipher"


def compute_plaintext(padding, precedent_cipher, enciphered_padding): # Every parameter is intended to be a byte
    return hex(padding ^ string_to_int(precedent_cipher) ^ string_to_int(enciphered_padding))[2:]


def compute_forged_cipher(padding, plaintext, precedent_cipher):
    '''
    Computes the cipher that corresponds to a given padding.
    The parameters should be bytes of the corresponding position

        Parameters:
            padding: The padding that we want the cipher to correspond to
            plaintext: the original plaintext that the original cipher decrypts to
            precedent_cipher: the original precedent cipher block

        Returns:
            The forged cipher
    '''
    return hex(padding ^ string_to_int(plaintext) ^ string_to_int(precedent_cipher))[2:]


def get_possible_enciphered_paddings(custom_cipher, padding) -> list:
    enciphered_paddings = list()
    custom_cipher = "".join(custom_cipher)
    for n in range(256):  # a byte
        if n < 16:
            n = '0' + hex(n)[2:]
        else:
            n = hex(n)[2:]
        payload = custom_cipher[:-2*padding] + n + (custom_cipher[-2*(padding-1):] if padding > 1 else "")
        
        # if n == '01':
        #     print(payload, end='')
        # elif n == 'ff':
        #     print(payload)
        # else:
        #     print('\033[2K\033[0G' + payload, end='')

        query = base64_equivalent_query(payload)

        result = correspondingQuery(query)
        print(payload + '\t' + result)
        if result == "Whack Computer Joke Database":
            enciphered_paddings.append(n)
    return enciphered_paddings


def string_to_int(string):
    return int('0x' + string, 16)


def string_to_hex(string):
    return hex(string_to_int(string))


if __name__ == "__main__":

    initialPageConnexion()

    # print(os.system("curl -s 'http://natas28.natas.labs.overthewire.org/search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKEMZKNASy09t5ooTNAbaX0vfoQVOxoUVz5bypVRFkZR5BPSyq%2FLC12hqpypTFR7gA%3D' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'DNT: 1' -H 'Authorization: Basic bmF0YXMyODpKV3dSNDM4d2tnVHNOS0JiY0pvb3d5eXNkTTgyWWplRg==' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'Cache-Control: max-age=0'"))

    # ciphertext_start = '1be82511a7ba5bfd578c0eef466db59cdc84728fdcf89d93751d10a7c75c8cf28431928d012cb4f6de68a133406da5f4bdfa1054ec68515cf96f2a5544591947'
    # ciphertext_start = '0000000000000000'
    # ciphertext_end = '86aa72a53151c95a'
    # with open('natas28/info.txt', 'a') as f:
    #     f.write('\n\n\n')
    #     for n in range(256):
    #         if n < 16:
    #             n = '0' + hex(n)[2:]
    #         else:
    #             n = hex(n)[2:]
    #         payload = ciphertext_start[:-2] + n # + ciphertext_start[-10:]
    #         print(payload)
    #         query = base64_equivalent_query(payload)
    #         f.write(f'query = {payload} {ciphertext_end}: {correspondingQuery(query)}\n')

    # print("\033[5mDone\033[0m") 

    # decrypt('904f4b2abf2c2d7686aa72a53151c970', 8) # TODO : Tester cette ligne sur mon desktop, elle ne fonctionne pas sur mon laptop
    decrypt('1be82511a7ba5bfd578c0eef466db59c', 8)
    