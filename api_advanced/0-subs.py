#!/usr/bin/python3
"""
Query the Reddit API for the number of subscribers of a subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers of a given subreddit.

    Return 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0.0 "
                             "(by deze-alu)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)
