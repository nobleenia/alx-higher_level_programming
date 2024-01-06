#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request
with the letter as a parameter
"""
from sys import argv
import requests


def main(argv):
    """
    Sends a POST request to url with the letter as a parameter
    """
    url = "http://0.0.0.0:5000/search_user"

    if len(argv) < 2:
        q = ""
    else:
        q = argv[2]

    mess = {"q": q}
    quest = requests.post(url, data=mess)

    try:
        feedback = quest.json()
        if bool(feedback) is False:
            print("No result")
        else:
            print("[{}] {}".format(feedback['id'], feedback['name']))
    except:
        print("Not a valid JSON")

if __name__ == "__main__":
    main(argv)
