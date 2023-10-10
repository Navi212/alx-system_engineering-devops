#!/usr/bin/python3
"""
A module that supplies a function that queries Reddit API and prints
first10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    headers = {"User-Agent": "Chrome/117.0.0.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    result = response.json().get("data")
    if (response.status_code == 404):
        print("None")
        return
    for i in result.get("children"):
        print(i.get("data").get("title"))
