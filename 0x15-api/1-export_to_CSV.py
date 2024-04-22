#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
Export data in the CSV format.
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    todos = requests.get(url + 'todos', params={'userId': user_id}).json()
    completed = [task.get('title') for task in todos if task.get('completed')]
    with open('{}.csv'.format(user_id), 'w') as file:
        for todo in todos:
            file.write(
                "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                    user_id,
                    user.get('username'),
                    todo.get('completed'),
                    todo.get('title')
                )
            )
