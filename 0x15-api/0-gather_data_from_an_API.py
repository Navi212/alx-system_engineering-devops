#!/usr/bin/python3
"""
The `0-gather_data_from_an_API` module fetches data
from an API and prints the result in stdout
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    user_id = argv[1]
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    posts_url = "https://jsonplaceholder.typicode.com/posts"
    user = requests.get(users_url).json()
    name = user.get("name")
    todo = requests.get(todos_url).json()
    c = 0
    u = 0
    for i in range(0, len(todo)):
        if (todo[i].get("userId") == int(user_id)):
            if (todo[i].get("completed")):
                c += 1
            elif not ((todo[i].get("completed"))):
                u += 1
    print(f"Employee {name} is done with tasks({c}/{c + u}):")
    for i in range(0, len(todo)):
        if (todo[i].get("userId") == int(user_id)):
            if (todo[i].get("completed")):
                print(f"\t {todo[i]['title']}")
