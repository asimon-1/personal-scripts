import requests
import re
import sys
import os
import pyperclip


def status_check(url):
    """Checks that the url can be reached.

    Arguments:
        url {string} -- Internet address to be checked.

    Returns:
        {boolean} -- True if the page was reached successfully.
    """

    response = requests.get(url)
    return response.status_code == 200


def post_to_url(url, data):
    """Sends a POST request to the webpage with specified payload.

    Arguments:
        url {string} -- Internet address to send to.
        data {dict} -- Payload of data to send along with the POST request.

    Returns:
        response -- The response to the POST request.
    """

    response = requests.post(url, data=data)
    return response


def extract_lorem_ipsum(response):
    """Finds the lorem ipsum text within the response.

    Arguments:
        response {response} -- The response of a GET or POST request.

    Returns:
        [string] -- The block of text within the preformatted tags designating
        the lorem ipsum output.
    """

    pattern = re.compile(r"""<pre id="htmlOutput".*>(.*)</pre>""", re.DOTALL)
    match_list = re.findall(pattern, response.text)
    if type(match_list) == list:
        return match_list[0]
    else:
        return match_list


def get_text(mode="PARAGRAPHS", howmany=3):
    """Wrapper function for the module, returns lorem ipsum text.

    Keyword Arguments:
        mode {str} -- What kind of text to get. Can be any of the following:
            "PARAGRAPHS", "SENTENCES", "WORDS", or "LIST_ITEMS"
            (default: {"PARAGRAPHS"})
        howmany {int} -- How many of the text blocks to get. (default: {3})

    Returns:
        str -- The returned text.
    """

    url = "https://www.freeformatter.com/lorem-ipsum-generator.html"
    data = {
        "type": "LOREMIPSUM",
        "mode": mode,
        "howMany": howmany,
        "size": "MEDIUM",
        "includeHtml": False,
    }

    status = status_check(url)
    assert status, "Could not reach Lorem Ipsum website!"
    response = post_to_url(url, data)
    text = extract_lorem_ipsum(response)

    return text


if __name__ == "__main__":
    args = sys.argv
    modes = ["PARAGRAPHS", "SENTENCES", "WORDS", "LIST_ITEMS"]
    mode = "PARAGRAPHS"
    howmany = 5
    for arg in args:
        if arg in modes:
            mode = arg
        try:
            howmany = int(arg)
        except ValueError:
            continue
    text = get_text(mode=mode, howmany=howmany)
    pyperclip.copy(text)
    print("Success! Copied lorem ipsum to clipboard.")
