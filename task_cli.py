import task_manager

def main():
    while True:
        entree = input('task > ').strip()
        
        # 2. Parsing basique
        parts = entree.split()
        if not parts: 
            continue
        command = parts[0]
        args = parts[1:]

        if command == 'exit':
            break
        elif command == 'load_tasks':
            tasks = task_manager.load_tasks() 
        elif command == 'add_task':
            task = task_manager.add_task('coucou')
        elif command == 'up':
            task_manager.update_task(1, 'update task')
        elif command == 'del':
            task_manager.delete_task(1)
        elif command == 'upd':
            task_manager.mark_status(1, 'done')

if __name__ == "__main__":
    main()