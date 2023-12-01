#!/usr/bin/python3
"""Sends a search request for a given string to the Star Wars API.

For each character matched, displays the associated list of movies.
Mangages pagination to display all results.

Usage: ./102-starwars.py <search string>
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

    for c, r in enumerate(results.get("results"), start=1):
        print(r.get("name"))
        for link in r.get("films"):
            film = requests.get(link).json()
            print("\t{}".format(film.get("title")))

    while results.get("next"):
        results = requests.get(results.get("next")).json()
        for r in results.get("results"):
            print(r.get("name"))
            for link in r.get("films"):
                film = requests.get(link).json()
                print("\t{}".format(film.get("title")))
