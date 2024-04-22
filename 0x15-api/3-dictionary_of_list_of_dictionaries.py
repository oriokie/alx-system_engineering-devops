#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
Python script to export data in the JSON format
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users').json()
    todos = requests.get(url + 'todos').json()
    users_dict = {}
    for user in users:
        user_id = user.get('id')
        user_todos = [task for task in todos if task.get('userId') == user_id]
        users_dict[user_id] = [{
            "username": user.get('username'),
            "task": task.get('title'),
            "completed": task.get('completed')
        } for task in user_todos]
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_dict, file)
