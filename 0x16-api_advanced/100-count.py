#!/usr/bin/python3
"""
module to get the top ten hot posts for a given subreddit
"""
import requests


def count_words(subreddit, word_list, after=None, counter={}):
    """
    function that queries the Reddit API and prints the titles of the first 10
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )
    if counter == {}:
        for word in word_list:
            counter[word.lower()] = 0

    if req.status_code == 200:
        after = req.json().get("data").get("after")
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            for word in word_list:
                counter[word.lower()] += title.lower()\
                    .split().count(word.lower())
        if after:
            return count_words(subreddit, word_list, after, counter)
        sorted(counter.items(), key=lambda x: x[1], reverse=True
               ).map(lambda x: x[1] and print(f"{x[0]} "))
    else:
        return None
