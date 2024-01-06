#!/usr/bin/python3
"""
Script takes a url and an email
Sends a POST request to url and  using email as param
Displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


def main(argv):
    """
    POST request to the passed URL with the email as a parameter
    """
    url = argv[1]
    var = {"email": argv[2]}
    post = urllib.parse.urlencode(var)
    post = post.encode("utf8")
    quest = urllib.request.Request(url, post)

    with urllib.request.urlopen(quest) as response:
        feedback = response.read()
        feed = feedback.decode("utf8")
        print(feed)

if __name__ == "__main__":
    main(argv)
