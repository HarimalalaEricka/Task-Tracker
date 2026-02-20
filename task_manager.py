import json

def load_tasks():
    f = open('task.json', 'r')
    tasks = json.load(f)
    return tasks