# Task Tracker CLI

A command-line application to manage your daily tasks.

> Project based on [roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)

---

## Prerequisites

- Python 3.x installed on your system

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/HarimalalaEricka/Task-Tracker.git
   cd Task-Tracker
   ```

2. No external dependencies required.

---

## Getting Started

Run the main file:

```bash
python task_cli.py
```

A command prompt `task-cli >` will appear, ready to receive your commands.

---

## Available Commands

| Command                       | Description |
|-------------------------------|-------------|
| `add <description>`           | Add a new task |
| `update <ID> <description>`   | Update a task's description |
| `del <ID>`                    | Delete a task |
| `mark-in-progress <ID>`       | Mark a task as in progress |
| `mark-done <ID>`              | Mark a task as done |
| `list`                        | Display all tasks |
| `list-by-date <date>`         | Filter tasks by creation date |
| `list-by-status <status>`     | Filter tasks by status |
| `list-sorted`                 | Display tasks sorted by date (most recent first) |
| `clear`                       | Clear the screen |
| `help`                        | Display help |
| `exit`                        | Quit the application |

---

## Usage Examples

### Add a task
```
task-cli > add Buy some bread
Task added.
```

### List all tasks
```
task-cli > list
Task list:
Created                 Updated                 ID      Status          Description
------------------------------------------------------------------------------------------
20/02/2026 10:30:00     20/02/2026 10:30:00     1       todo            Buy some bread
```

### Update a task
```
task-cli > update 1 Buy bread and milk
Task updated.
```

### Mark a task as in progress
```
task-cli > mark-in-progress 1
Task marked as in progress.
```

### Mark a task as done
```
task-cli > mark-done 1
Task marked as done.
```

### Delete a task
```
task-cli > del 1
Task deleted.
```

### Filter by status
```
task-cli > list-by-status todo
task-cli > list-by-status in-progress
task-cli > list-by-status done
```

### Filter by date
```
task-cli > list-by-date 20/02/2026
```

---

## Task Statuses

| Status | Description |
|--------|-------------|
| `todo` | Task to do (default status) |
| `in-progress` | Task in progress |
| `done` | Task completed |

---

## Data Storage

Tasks are saved in the `task.json` file in JSON format. This file is automatically created on first use.

---

## Task Structure

```json
{
    "id": 1,
    "description": "My task",
    "status": "todo",
    "createdAt": "20/02/2026 10:30:00",
    "updatedAt": "20/02/2026 10:30:00"
}
```

---

## License

This project is free to use.