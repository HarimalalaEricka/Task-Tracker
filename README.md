# Task Tracker CLI

Une application en ligne de commande pour gérer vos tâches quotidiennes.

> Projet basé sur [roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)

---

## Prérequis

- Python 3.x installé sur votre système

---

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/HarimalalaEricka/Task-Tracker.git
   cd Task-Tracker
   ```

2. Aucune dépendance externe n'est requise.

---

## Lancement

Exécutez le fichier principal :

```bash
python task_cli.py
```

Une invite de commande `task-cli >` apparaîtra, prête à recevoir vos commandes.

---

## Commandes disponibles

| Commande                      | Description |
|-------------------------------|-------------|
| `add <description>`           | Ajouter une nouvelle tâche |
| `update <ID> <description>`   | Modifier la description d'une tâche |
| `del <ID>`                    | Supprimer une tâche |
| `mark-in-progress <ID>`       | Marquer une tâche comme en cours |
| `mark-done <ID>`              | Marquer une tâche comme terminée |
| `list`                        | Afficher toutes les tâches |
| `list-by-date <date>`         | Filtrer les tâches par date de création |
| `list-by-status <status>`     | Filtrer les tâches par statut |
| `list-sorted`                 | Afficher les tâches triées par date (récent en premier) |
| `clear`                       | Effacer l'écran |
| `help`                        | Afficher l'aide |
| `exit`                        | Quitter l'application |

---

## Exemples d'utilisation

### Ajouter une tâche
```
task-cli > add Acheter du pain
Tâche ajoutée.
```

### Lister toutes les tâches
```
task-cli > list
Liste des tâches :
Created                 Updated                 ID      Status          Description
------------------------------------------------------------------------------------------
20/02/2026 10:30:00     20/02/2026 10:30:00     1       todo            Acheter du pain
```

### Mettre à jour une tâche
```
task-cli > update 1 Acheter du pain et du lait
Tâche mise à jour.
```

### Marquer une tâche en cours
```
task-cli > mark-in-progress 1
Tâche marquée comme en cours.
```

### Marquer une tâche comme terminée
```
task-cli > mark-done 1
Tâche marquée comme terminée.
```

### Supprimer une tâche
```
task-cli > del 1
Tâche supprimée.
```

### Filtrer par statut
```
task-cli > list-by-status todo
task-cli > list-by-status in-progress
task-cli > list-by-status done
```

### Filtrer par date
```
task-cli > list-by-date 20/02/2026
```

---

## Statuts des tâches

| Statut | Description |
|--------|-------------|
| `todo` | Tâche à faire (statut par défaut) |
| `in-progress` | Tâche en cours |
| `done` | Tâche terminée |

---

## Stockage des données

Les tâches sont sauvegardées dans le fichier `task.json` au format JSON. Ce fichier est créé automatiquement lors de la première utilisation.

---

## Structure d'une tâche

```json
{
    "id": 1,
    "description": "Ma tâche",
    "status": "todo",
    "createdAt": "20/02/2026 10:30:00",
    "updatedAt": "20/02/2026 10:30:00"
}
```

---

## Licence

Ce projet est libre d'utilisation.