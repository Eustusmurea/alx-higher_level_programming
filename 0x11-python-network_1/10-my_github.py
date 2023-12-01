#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Check if the required command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: {} <GitHub username> <GitHub password>".format(sys.argv[0]))
        sys.exit(1)

    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)

    # Check if the request was successful and if the response is valid JSON
    if r.status_code == 200:
        try:
            user_id = r.json().get("id")
            print("GitHub ID:", user_id)
        except ValueError:
            print("Invalid JSON in response.")
    else:
        print("Error: {}".format(r.status_code))
