#!/usr/bin/python3
"""
Script that takes your GitHub credentials,
and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main(argv):
    """
    Access GitHub API (username & password),
    and uses the information to display ID
    """
    user = argv[1]
    password = argv[2]
    feedback = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(user, password))
    try:
        profile_data = feedback.json()
        print(profile_data["id"])
    except:
        print("None")

if __name__ == "__main__":
    main(argv)
