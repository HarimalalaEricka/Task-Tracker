import json
import datetime

def load_tasks():
    f = open('task.json', 'r')
    tasks = json.load(f)
    return tasks

def save_tasks(tasks):
    f = open('task.json', 'w')
    json.dump(tasks, f, indent=4)

def add_task(task):
    tasks = load_tasks()
    last_task = tasks[-1]
    last_id = last_task['id']
    new_id = last_id + 1
    status = 'todo'
    createdAt = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    updatedAt = createdAt
    new_task = { 
        'id': new_id,
        'description': task,
        'status': status,
        'createdAt': createdAt,
        'updatedAt': updatedAt
    }
    tasks.append(new_task)
    save_tasks(tasks)

def update_task(id, desc):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == id:
            task['description'] = desc
    save_tasks(tasks)

def delete_task(id):
    tasks = load_tasks()
    for task in tasks:  
        if task['id'] == id:
            tasks.remove(task)
            break  
    save_tasks(tasks)