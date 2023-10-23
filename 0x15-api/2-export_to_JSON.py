#!/usr/bin/python3
"""api to json"""
import json
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

    dictinary = {emp_id: []}
    for task in todo_js:
        dictinary[emp_id].append({"task": task.get("title"),
                                  "completed": task.get("completed"),
                                  "username": emp_name})

    with open("{}.json".format(emp_id), "w") as file:
        json.dump(dictinary, file)
