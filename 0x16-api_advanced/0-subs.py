#!/usr/bin/python3
"""Queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    headers = {"User-Agent": "Chrome/117.0.0.0"}
    url = f"https://www.reddit.com/r/{subreddit}/.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return (0)
    result = response.json().get("data")
    sub = result.get("subscribers")
    return (sub)
