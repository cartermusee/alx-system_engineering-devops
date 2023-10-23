#!/usr/bin/python3
"""module for api saving to csv"""
import requests
from sys import argv


if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com/users"
    emp_id = argv[1]

    url = base_url + "/" + emp_id
    api_req = requests.get(url)
    emp_name = api_req.json().get("username")

    todo = url + "/todos"
    todo_res = requests.get(todo)
    todo_js = todo_res.json()

    with open("{}.csv".format(emp_id), "w") as file:
        for task in todo_js:
            file.write('"{}","{}","{}","{}"\n'.
                       format(emp_id, emp_name, task.get('completed'),
                              task.get('title')))
