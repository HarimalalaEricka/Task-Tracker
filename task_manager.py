import json
import datetime
import os

def load_tasks():
    if not os.path.exists('task.json'):
        with open('task.json', 'w') as f:
            json.dump([], f)
    with open('task.json', 'r') as f:
        tasks = json.load(f)
        return tasks
    
def isIDExist(id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == id:
            return True
    return False

def save_tasks(tasks):
    f = open('task.json', 'w')
    json.dump(tasks, f, indent=4)

def add_task(task):
    tasks = load_tasks()
    if tasks:
        last_id = tasks[-1]['id']
        new_id = last_id + 1    
    else:
        new_id = 1
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
    if not isIDExist(id):
        print(f"Erreur : Tâche avec ID {id} n'existe pas.")
        return
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == id:
            task['description'] = desc
    save_tasks(tasks)
    print("Tâche mise à jour.")


def delete_task(id):
    if not isIDExist(id):
        print(f"Erreur : Tâche avec ID {id} n'existe pas.")
        return
    tasks = load_tasks()
    for task in tasks: 
        if task['id'] == id:
            tasks.remove(task)
            break  
    save_tasks(tasks)
    print("Tâche supprimée.")


def mark_status(id, status):
    if not isIDExist(id):
        print(f"Erreur : Tâche avec ID {id} n'existe pas.")
        return
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == id:
            task['status'] = status
            task['updatedAt'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    save_tasks(tasks)
    if status == 'in-progress':
        print("Tâche marquée comme en cours.")
    elif status == 'done':
        print("Tâche marquée comme terminée.")


def list_task():
    tasks = load_tasks()
    print("Liste des tâches :")
    print("Created\t\t\tUpdated\t\t\tID\tStatus\t\tDescription")
    print("-" * 90)
    for task in tasks:
        print(f"{task['createdAt']}\t{task['updatedAt']}\t{task['id']}\t{task['status']:<10}\t{task['description'][:30]:<30}")