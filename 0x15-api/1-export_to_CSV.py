#!/usr/bin/python3
"""Python script that, using a REST API, for a given employee ID,
returns information about his/her and export data in the CSV format."""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
        ).json()
    all_tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"
        ).json()
    with open(f"{argv[1]}.csv", "w") as f:
        csv_file = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in all_tasks:
            csv_file.writerow([user['id'], user['username'],
                              task['completed'], task['title']])
