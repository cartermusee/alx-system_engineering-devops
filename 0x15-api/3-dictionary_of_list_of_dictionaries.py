#!/usr/bin/python3
"""json all users"""
import requests
import json
from sys import argv


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/users"

    api_req = requests.get(url)
    users = api_req.json()

    dictinary = {}
    for user in users:
        emp_id = user.get("id")
        emp_name = user.get("username")
        url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
        todo = url + "/todos"
        todo_res = requests.get(todo)
        todo_js = todo_res.json()

        dictinary = {emp_id: []}
        for task in todo_js:
            dictinary[emp_id].append({"username": emp_name,
                                      "task": task.get("title"),
                                      "completed": task.get("completed"), })

        with open("todo_all_employees.json", "w") as file:
            json.dump(dictinary, file)
