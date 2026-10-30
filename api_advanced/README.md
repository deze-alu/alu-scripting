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

## Usage

```
$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0
```
