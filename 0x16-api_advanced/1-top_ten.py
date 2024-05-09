#!/usr/bin/python3
"""
Prints the titles of the hottest posts on a given subreddit
"""
import requests


def top_ten(subreddit):
    """Function for retrieving top 10 hot posts"""
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10'
    response = requests.get(url, headers={'User-agent': 'Rbot v1'},
                            allow_redirects=False).json()
    if 'error' in response:
        print(None)
        return
    hot_posts = response.get("data", {}).get("children", [])
    for post in hot_posts:
        print(post.get("data", {}).get("title", None))
