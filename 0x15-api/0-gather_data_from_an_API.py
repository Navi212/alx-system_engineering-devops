#!/usr/bin/python3
"""
The `0-gather_data_from_an_API` that fetches data
from API
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    todos_url = f"https://jsonplaceholder.typicode.com/todos"
    users_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    posts_url = f"https://jsonplaceholder.typicode.com/posts"
    user = requests.get(users_url).json()
    name = user["name"]
    todo = requests.get(todos_url).json()
    c = 0
    u = 0
    for i in range(0, len(todo)):
        if (todo[i]["userId"] == int(argv[1])):
            if (todo[i]["completed"]):
                c += 1
            elif not ((todo[i]["completed"])):
                u += 1
    print(f"Employee {name} is done with tasks({c}/{c + u}):")
    for i in range(0, len(todo)):
        if (todo[i]["userId"] == int(argv[1])):
            if (todo[i]["completed"]):
                print(f"\t{todo[i]['title']}")
