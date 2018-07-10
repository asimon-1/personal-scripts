'''thesaurus.py
Author: AJS 12/2017 To use, enter a command prompt in the same directory where
this file lives and use the following syntax
>> python thesaurus.py lookupword'''

import requests
import re
import sys
import os
os.system('cls')  # Clear command prompt window

# Use command line argument if possible, otherwise default input is "good" for
# testing.
try:
    word = sys.argv[1]
except:
    word = 'good'

# Request the synonyms for the specified word
version = 2
with open('thesaurus_api.key', 'r') as f:
    apikey = f.read()
fmt = ''

url = 'http://words.bighugelabs.com/api/{}/{}/{}/{}'.format(version, apikey, word, fmt)
r = requests.get(url)
assert r.status_code in [200, 303], (
    "Error getting response from URL: {}\n\nStatus Code was {}".format(
        url, r.status_code))

# WPrint all of the listed synonyms
print("\nSynonyms for \"{}\" are:\n".format(word))
print(r.text)
