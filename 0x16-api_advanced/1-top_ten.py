#!/usr/bin/python3

"""
irst 10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """function 
    args:
        subreddit:subreddit"""

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    headers = {
        'User-Agent': 'MyApi/0.0.1'
    } 
    limit = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    
    response = get(url, headers=headers, params=limit)
    results = response.json()

    try:
        data = results.get('data').get('children')

        for i in data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
