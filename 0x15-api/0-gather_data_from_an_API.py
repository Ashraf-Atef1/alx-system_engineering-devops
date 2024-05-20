#!/usr/bin/python3
"""Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress."""
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
    completed_tasks = [task for task in all_tasks if task['completed']]
    print(f"Employee {user['name']} is done with \
tasks({len(completed_tasks)}/{len(all_tasks)}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")
