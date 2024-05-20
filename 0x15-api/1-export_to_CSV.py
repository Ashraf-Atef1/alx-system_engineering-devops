#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
from json import loads
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    user = loads(user.text)
    all_tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}")
    all_tasks = loads(all_tasks.text)
    with open(f"{argv[1]}.csv", "w") as f:
        for task in all_tasks:
            f.write(f'"{user['id']}","{user['username']}",\
"{task['completed']}","{task['title']}"\n')
