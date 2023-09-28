#!/usr/bin/python3
"""
The `2-export_to_JSON` module fetches data
from API and exports a particular user_id data
to JSON File
"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv
    user_id = argv[1]
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user = requests.get(users_url).json()
    todo = requests.get(todos_url).json()
    username = user.get("username")
    filename = f"{user_id}.json"
    dit_list = {}
    dit = {}
    li = []
    with open(filename, "w") as jfile:
        for i in range(0, len(todo)):
            if (todo[i].get("userId") == int(user_id)):
                dit_list = {
                        "task": todo[i].get("title"),
                        "completed": todo[i].get("completed"),
                        "username": username
                        }
                li.append(dit_list)
        dit[f"{user_id}"] = li
        json.dump(dit, jfile)
