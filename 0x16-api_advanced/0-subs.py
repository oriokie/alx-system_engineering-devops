#!/usr/bin/python3
"""
Function that queries the Reddit API and then returns the number of
subsribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of the total subscribers for a subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return (0)

    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'

    response = requests.get(url, headers={'User-agent': 'Rbot v1'},
                            allow_redirects=False).json()
    subs = response.get("data", {}).get("subscribers", 0)
    return (subs)
