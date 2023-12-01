#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests

if __name__ == "__main__":
    # Check if the required command-line arguments are provided
    if len(sys.argv) != 3:
        print(
            "Usage: {} <repository name> <repository owner>".format(
                sys.argv[0]))
        sys.exit(1)

    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)

    # Check if the request was successful and if the response is valid JSON
    if r.status_code == 200:
        commits = r.json()
        if len(commits) < 10:
            print("Less than 10 commits available.")
        else:
            for i in range(10):
                print("{}: {}".format(
                    commits[i].get("sha"),
                    commits[i].get("commit").get("author").get("name")))
    else:
        print("Error: {}".format(r.status_code))
