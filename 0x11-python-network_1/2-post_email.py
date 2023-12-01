#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Check if the required command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data for the POST request
    data = {"email": email}
    data_encoded = urllib.parse.urlencode(data).encode("ascii")

    # Send the POST request
    request = urllib.request.Request(url, data=data_encoded)
    try:
        with urllib.request.urlopen(request) as response:
            # Print the body of the response
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("HTTPError: {}".format(e))
    except urllib.error.URLError as e:
        print("URLError: {}".format(e))
    except Exception as e:
        print("Error: {}".format(e))
