#!/usr/bin/python3

"""
queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """print the titles of the 10 hottest posts on a given subreddit"""
    try:
        url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
        headers = {"User-Agent": "chibuokem"}
        params = {"limit": 10}
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        result = response.json().get("data")
        for i in result.get("children"):
            print(i.get('data').get('title'))
    except AttributeError:
        print(None)
