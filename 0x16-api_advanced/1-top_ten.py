#!/usr/bin/python3
"""A 1-top_ten module"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Chrome 199929"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    result = response.json().get("data")
    if (response.status_code == 404):
        return (0)
    li = []
    for i in result.get("children"):
        li.append(i.get("data").get("title"))
    print(li)
