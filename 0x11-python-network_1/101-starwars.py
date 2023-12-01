#!/usr/bin/python3
"""Sends a search request for a given string to the Star Wars API.

Mangages pagination to display all results.

Usage: ./101-starwars.py <search string>
  - The search request is sent to the Star Wars API search people endpoint.
"""
import sys
import requests


def get_results(url, params):
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print("Error: Unable to fetch data from SWAPI. Status code: {}".format(response.status_code))
        sys.exit(1)

    return response.json()


if __name__ == "__main__":
    # Check if the required command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: {} <search string>".format(sys.argv[0]))
        sys.exit(1)

    search_query = sys.argv[1]
    url = "https://swapi.co/api/people"
    params = {"search": search_query}
    results = get_results(url, params)

    count = results.get("count")
    print("Number of results: {}".format(count))

    c = 0
    while c < count:
        for r in results.get("results"):
            print(r.get("name"))
            c += 1

        next_page = results.get("next")
        if next_page is not None:
            results = get_results(next_page, {})  # Send a request to the next page
        else:
            break

