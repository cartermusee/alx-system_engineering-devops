#!/usr/bin/python3
"""modeule for a rest api"""
from sys import argv
import requests


if __name__ == "__main__":

    base_url = 'https://jsonplaceholder.typicode.com/user'
    emp_id = argv[1]

    url = base_url + "/" + emp_id
    api_req = requests.get(url)
    emp_name = api_req.json().get('name')

    todo = url + "/todos"
    todo_res = requests.get(todo)
    todo_js = todo_res.json()
    tasks = 0
    task_done = []

    for task in todo_js:
        if task.get("completed"):
            task_done.append(task)
            tasks += 1
    print("Employee {} is done with tasks ({}/{})".
          format(emp_name, tasks, len(todo_js)))

    for task in task_done:
        print("\t {}".format(task.get("title")))
