#!/usr/bin/python3
"""
Recursively query the Reddit API, parse the titles of all hot articles
of a subreddit, and print a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, tokens=[]):
    """Print a sorted count of the given keywords in all hot article titles.

    Follow Reddit's pagination by calling itself with the after token
    of each page, collecting the lowercase words of every title. Print
    nothing if the subreddit is invalid or no keyword matches.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0.0 "
                             "(by deze-alu)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print_counts(word_list, tokens)
        return

    data = response.json().get("data", {})
    titles = map(lambda post: post.get("data", {}).get("title", ""),
                 data.get("children", []))
    tokens = tokens + " ".join(titles).lower().split()
    after = data.get("after")
    if after is None:
        print_counts(word_list, tokens)
        return
    count_words(subreddit, word_list, after, tokens)


def print_counts(word_list, tokens):
    """Print how many times each keyword appears in tokens.

    Duplicate keywords add up, results are sorted by count (descending)
    then alphabetically, and keywords with no matches are skipped.
    """
    words = list(map(str.lower, word_list))
    counts = map(lambda word: (word, tokens.count(word) * words.count(word)),
                 set(words))
    matches = sorted(filter(lambda item: item[1] > 0, counts),
                     key=lambda item: (-item[1], item[0]))
    if matches:
        print("\n".join(map(lambda item: "{}: {}".format(*item), matches)))
