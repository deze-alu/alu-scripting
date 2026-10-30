# API advanced

Python functions that query the [Reddit API](https://www.reddit.com/dev/api/)
to read subreddit data, follow pagination recursively, and parse and sort
the results.

## Requirements

- Ubuntu 14.04 LTS
- Python 3.4.3
- `requests` module
- PEP 8 style

## Files

| File | Description |
| ---- | ----------- |
| `0-subs.py` | `number_of_subscribers(subreddit)`: return the total number of subscribers of a subreddit, or 0 if it is invalid |
| `1-top_ten.py` | `top_ten(subreddit)`: print the titles of the first 10 hot posts of a subreddit, or None if it is invalid |
| `2-recurse.py` | `recurse(subreddit, hot_list=[])`: recursively return a list of the titles of all hot articles of a subreddit, or None if none are found |
| `3-count.py` | `count_words(subreddit, word_list)`: recursively count given keywords in all hot article titles of a subreddit and print them sorted by count, then alphabetically |

## Usage

```
$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0
$ python3 1-main.py programming
Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
...
$ python3 1-main.py this_is_a_fake_subreddit
None
$ python3 2-main.py programming
932
$ python3 2-main.py this_is_a_fake_subreddit
None
$ python3 3-main.py programming 'react python java javascript scala no_results_for_this_one'
java: 27
javascript: 20
python: 17
react: 17
scala: 4
$ python3 3-main.py programming 'JavA java'
java: 54
$ python3 3-main.py not_a_valid_subreddit 'python java'
$
```
