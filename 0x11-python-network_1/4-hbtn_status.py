#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


def main():
    """
    Fetches https://intranet.hbtn.io/status
    """
    url = "https://alx-intranet.hbtn.io/status"
    quest = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(quest.text)))
    print("\t- content: {}".format(quest.text))

if __name__ == "__main__":
    main()
