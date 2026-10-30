#!/usr/bin/python3
"""
Query the Reddit API for the titles of the first 10 hot posts
of a subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a given subreddit.

    Print None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0.0 "
                             "(by deze-alu)"}
    response = requests.get(url, headers=headers, params={"limit": 10},
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data", {}).get("children", [])
    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
