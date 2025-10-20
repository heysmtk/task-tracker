import argparse
from models import TaskManager
from utils import menu


# Task Manager - manager (creating instance)
manager = TaskManager()

# Argument Parser - commands for cli interaction
parser = argparse.ArgumentParser(description="Task Tracker CLI app")
parser.add_argument("action", choices=["add", "update", "delete", "done","progress", "list-all", "list-done"], help="Akce s úkoly")
parser.add_argument("id", nargs="?", help="ID úkolu")
parser.add_argument("value", nargs="?", help="Popis úkolu nebo nový úkol")

# Load arguments from command line
args = parser.parse_args()


# App logic
if args.action == "add":
    description = args.value or args.id
    manager.add_task(description)
    print(f"Task was added: {description}")
elif args.action == "update":
    manager.update_task(int(args.id), args.value)
    print(f"Task (ID:{args.id}) was changed: {args.value}")
elif args.action == "delete":
    manager.delete_task(int(args.id))
    print(f"Task (ID:{args.id}) was deleted.")
elif args.action == "done":
    manager.mark_task_done(int(args.id))
    print(f"Task (ID:{args.id}) is marked as done.")
elif args.action == "progress":
    manager.mark_task_in_progress(int(args.id))
    print(f"Task (ID:{args.id}) is marked as in progress.")
elif args.action == "list-all":
    manager.list_all_tasks()
elif args.action == "list-done":
    manager.list_done_tasks()