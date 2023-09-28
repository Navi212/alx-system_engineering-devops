#!/usr/bin/python3
"""
The `2-export_to_JSON` that fetches data
from API an exports to JSON File
"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv
    user_id = argv[1]
    todos_url = f"https://jsonplaceholder.typicode.com/todos"
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
                dit_list["task"] = todo[i]["title"]
                dit_list["completed"] = todo[i]["completed"]
                dit_list["username"] = username
                li.append(dit_list)
        dit[f"{user_id}"] = li
        json.dump(dit, jfile)
