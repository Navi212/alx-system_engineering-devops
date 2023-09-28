#!/usr/bin/python3
"""
The `2-export_to_JSON` that fetches data
from API an exports to JSON File
"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = f"https://jsonplaceholder.typicode.com/users"
    user = requests.get(users_url).json()
    todo = requests.get(todos_url).json()
    filename = "todo_all_employees.json"
    dit_list = {}
    dit = {}
    li = []
    with open(filename, "w") as jfile:
        for i in range(0, len(todo)):
            for j in range(0, len(user)):
                dit_list = {
                    "task": todo[i].get("title"),
                    "completed": todo[i].get("completed"),
                    "username": user[j].get("username")
                    }
                user_id = todo[i].get("userId")
                li.append(dit_list)
                dit[f"{user_id}"] = li
        json.dump(dit, jfile)
