#!/usr/bin/python3
"""Get the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    """
    r = requests.get(
            'http://www.reddit.com/r/{}/about.json'.format(subreddit),
            headers={'User-Agent': 'Redditbot'})
    r = r.json()
    try:
            return(int(r['data']['subscribers']))
    except:
            return(0)
