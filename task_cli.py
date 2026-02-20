import task_manager
import os

def main():
    while True:
        entree = input('task-cli > ').strip()
        
        # 2. Parsing basique
        parts = entree.split()
        if not parts: 
            continue
        command = parts[0]
        args = parts[1:]

        if command == 'exit':
            break
        elif command == 'add':
            task_manager.add_task(' '.join(args))
            print("Tâche ajoutée.")
        elif command == 'update':
            if len(args) >= 2:
                try:
                    task_id = int(args[0])
                    description = ' '.join(args[1:])
                    task_manager.update_task(task_id, description)
                except ValueError:
                    print("Erreur : l'ID doit être un nombre.")
            else:
                print("Usage : update <ID> <description>")
        elif command == 'del':
            task_manager.delete_task(int(args[0]))
        elif command == 'mark-in-progress':
            if len(args) >= 1:
                try:
                    task_id = int(args[0])
                    task_manager.mark_status(task_id, 'in-progress')
                except ValueError:
                    print("Erreur : l'ID doit être un nombre.")
            else:
                print("Usage : mark-in-progress <ID>")
        elif command == 'mark-done':
            if len(args) >= 1:
                try:
                    task_id = int(args[0])
                    task_manager.mark_status(task_id, 'done')
                except ValueError:
                    print("Erreur : l'ID doit être un nombre.")
            else:
                print("Usage : mark-done <ID>")
        elif command == 'list':
            task_manager.list_task()
        elif command == 'clear':
            os.system('cls')
        elif command == 'help':
            print("Commandes disponibles :")
            print("  add <description>          - Ajouter une nouvelle tâche")
            print("  update <ID> <description>  - Mettre à jour la description d'une tâche")
            print("  del <ID>                   - Supprimer une tâche")
            print("  mark-in-progress <ID>      - Marquer une tâche comme en cours")
            print("  mark-done <ID>             - Marquer une tâche comme terminée")
            print("  list                       - Lister toutes les tâches")
            print("  clear                      - Effacer l'écran")
            print("  help                       - Afficher cette aide")
            print("  exit                       - Quitter l'application")
        else:
            print('Command not found')

if __name__ == "__main__":
    main()