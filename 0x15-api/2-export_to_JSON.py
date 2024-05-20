#!/usr/bin/python3
"""Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress."""
from json import dump
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
        ).json()
    all_tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"
        ).json()
    with open(f"{user['id']}.json", "w") as json_file:
        dump({user['id']: [{
                "task": task['title'],
                "completed": task['completed'],
                "username": user['username']
            } for task in all_tasks]}, json_file)
