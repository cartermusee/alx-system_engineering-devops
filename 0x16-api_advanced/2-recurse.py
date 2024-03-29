#!/usr/bin/python3
"""module for recurse it"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """function
    args:
        subreddit:subreddit
        hot_list:list
        after:after
        count:keep count"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        'User-Agent': 'MyApi/0.0.1'
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
