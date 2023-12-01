#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
     if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
