#!/usr/bin/python3
"""Sends a search request for a given string to the Star Wars API.

Usage: ./9-starwars.py <search string>
  - The search request is sent to the Star Wars API search people endpoint.
"""
import sys
import requests

if __name__ == "__main__":
    # Check if the required command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: {} <search string>".format(sys.argv[0]))
        sys.exit(1)

    url = "https://swapi.co/api/people"
    params = {"search": sys.argv[1]}
    results = requests.get(url, params=params).json()

    print("Number of results: {}".format(results.get("count")))

    # Check if there are any results before attempting to print them
    if not results.get("results"):
        print("No results found.")
    else:
        [print(r.get("name")) for r in results.get("results")]
