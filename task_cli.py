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
        print(args)

        if command == 'exit':
            break
        elif command == 'load_tasks':
            tasks = task_manager.load_tasks() 
            print(tasks)

if __name__ == "__main__":
    main()