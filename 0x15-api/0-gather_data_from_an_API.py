#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    todos = requests.get(url + 'todos', params={'userId': user_id}).json()
    completed = [task.get('title') for task in todos if task.get('completed')]
    print('Employee {} is done with tasks({}/{}):'.format(user.get('name'),
                                                          len(completed),
                                                          len(todos)))
    [print('\t {}'.format(task)) for task in completed]
