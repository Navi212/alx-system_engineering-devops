#!/usr/bin/python3
"""
The `1-export_to_CSV` that fetches data
from API an exports to CSV File
"""
if __name__ == "__main__":
    import csv
    import requests
    from sys import argv
    user_id = argv[1]
    todos_url = f"https://jsonplaceholder.typicode.com/todos"
    users_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user = requests.get(users_url).json()
    todo = requests.get(todos_url).json()
    name = user.get("name")
    username = user.get("username")

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        obj = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_ALL)
        for i in range(0, len(todo)):
            if (todo[i]["userId"] == int(user_id)):
                status = todo[i].get("completed")
                title = todo[i].get("title")
                obj.writerow([user_id, username, status, title])
