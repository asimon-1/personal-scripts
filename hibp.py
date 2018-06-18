"""This script checks the given command line argument (either an email or password) against the Have I Been Pwned
data breach database.
"""

import sys
import requests
from hashlib import sha1


def check_password(password):
    hsh = sha1()
    hsh.update(password.encode('utf-8'))
    h = hsh.hexdigest()
    response = requests.get('https://api.pwnedpasswords.com/range/{}'.format(h[0:5])).text.lower().split('\n')
    for line in response:
        if h[5:] in line:
            return 'Password \"{0}\" was detected a total of {1} times!'.format(password, line[line.find(':')+1:-1])
    return 'Password was not found in the HIBP database. Still be skeptical though!'


def check_account(account): #TODO: fix bug in this function
    response = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/{}'.format(account))
    print(response.text)
    return None

if __name__ == "__main__":
    cmd_input = sys.argv[1]
    if '.com' in cmd_input:
        cmd_output = check_account(cmd_input)
    else:
        cmd_output = check_password(cmd_input)
    print(cmd_output)
