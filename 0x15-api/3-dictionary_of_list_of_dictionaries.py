#!/usr/bin/python3
"""Python script that, using a REST API, returns information
about all employees TODO list in a json file."""
from json import dump
import requests
from sys import argv

if __name__ == "__main__":
    users = requests.get(
        f"https://jsonplaceholder.typicode.com/users/"
        ).json()
    all_tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/todos"
        ).json()
    with open("todo_all_employees.json", "w") as json_file:
        all_data = {}
        for user in users:
            user_tasks = [task for task in all_tasks
                          if task['userId'] == user['id']]
            all_data[user['id']] = [{
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": user['username']
                } for task in user_tasks]
        dump(all_data, json_file)
