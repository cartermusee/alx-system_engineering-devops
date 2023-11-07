#!/usr/bin/python3
"""module for sub"""
import requests


def number_of_subscribers(subreddit):
    """function
    args:
        subreddit:subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'MyApi/0.0.1'
    } 
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
