import os
import urllib.request as url
import urllib.parse
import time

NATAS_URL = 'http://natas28.natas.labs.overthewire.org'
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
    my_url = output.url

    return my_url[my_url.find('=')+1:]


if __name__ == "__main__":

    initialPageConnexion()

    # =======================================================================================
    # This part creates a list of letters that are in the password. I commented it out
    # because it takes some time to run so I want to avoid running it too often
    # =======================================================================================

    with open('natas28/info.txt', 'a') as f:
        for i in range(1, 30) :
            string = '\x00' * i
            print('Performing ' + string + '...')
            f.write(string + ':\t' + urllib.parse.unquote(correspondingQuery(string)) + '\n')