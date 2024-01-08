#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest)
Of the repository “rails” by the user “rails”
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


def main(argv):
    """
    List 10 commits (from the most recent to oldest)
    """
    def list_commits(i, commit_list):
        """
        Prints all the commits by, `sha` and `author`
        """
        sha = commit_list[i].get("sha")
        commit = commit_list[i].get("commit")
        author = commit.get("author")
        name = author.get("name")
        print('{}: {}'.format(sha, name))

    repository_name = argv[1]
    owner_name = argv[2]
    headers = {"Accept": "application/vnd.github.v3+json"}
    feedback = requests.get("https://api.github.com/repos/" + owner_name
                            + "/" + repository_name + "/commits", headers=headers)
    commit_list = feedback.json()
    size = len(commit_list)

    if size < 10:
        for i in range(0, size):
            list_commits(i, commit_list)
    else:
        for i in range(0, 10):
            list_commits(i, commit_list)


if __name__ == "__main__":
    main(argv)
