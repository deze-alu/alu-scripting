#!/usr/bin/python3
"""
Recursively query the Reddit API to collect the titles of all hot
articles of a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list containing the titles of all hot articles of a subreddit.

    Follow Reddit's pagination by calling itself with the after token
    of each page. Return None if the subreddit is invalid or has no
    hot articles.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0.0 "
                             "(by deze-alu)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return hot_list or None

    data = response.json().get("data", {})
    titles = list(map(lambda post: post.get("data", {}).get("title"),
                      data.get("children", [])))
    hot_list = hot_list + titles
    after = data.get("after")
    if after is None:
        return hot_list or None
    return recurse(subreddit, hot_list, after)
