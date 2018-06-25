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

# Request the thesaurus.com page for the specified word
url = 'http://www.thesaurus.com/browse/{}'.format(word)
r = requests.get(url)
assert r.status_code == 200, (
    "Error getting response from URL: {}\n\nStatus Code was {}".format(
        url, r.status_code))

# Find all div elements which contain synonyms. This website handles multiple
# homographs by putting them in separate divs. This shows up as separate tabs
# on the web page.
pattern_div = re.compile(r"""<div class=\"relevancy-list\">(.*?)</div>""",
                         re.DOTALL)
pattern_syn = re.compile(
    r"""<li><a href=\"http://www\.thesaurus\.com/browse/(\w+)\" (?:class=\"common-word\")? data-id=""",
    re.DOTALL)
syn_list = re.findall(pattern_div, r.text)
assert syn_list is not None, "No synonym divs found!"

# Within each synonym division, print all of the listed synonyms
print("\nSynonyms for \"{}\" are:\n".format(word))
for l in syn_list:
    results = re.findall(pattern_syn, l)
    assert results is not None, "No synonym results found!"
    print('\n'.join(results))
