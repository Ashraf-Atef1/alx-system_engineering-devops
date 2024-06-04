#!/usr/bin/python3
"""
module to get the top ten hot posts for a given subreddit
"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    function that queries the Reddit API and prints the titles of the first 10
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if req.status_code == 200:
        after = req.json().get("data").get("after")
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        if after:
            recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return hot_list
