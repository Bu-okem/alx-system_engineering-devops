#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        r = requests.get(url, headers={'User-agent': 'chibuokem'})
        subs = r.json()
        return subs.get('data').get('subscribers')
    except AttributeError:
        return 0
