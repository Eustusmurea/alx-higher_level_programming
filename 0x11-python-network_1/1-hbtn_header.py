#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request

if __name__ == "__main__":
    # Check if the required command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        # Check if the "X-Request-Id" header is present in the response
        x_request_id = response.headers.get("X-Request-Id")
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")

