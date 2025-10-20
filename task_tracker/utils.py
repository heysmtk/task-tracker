import argparse

menu = """
=======MENU======
1. My tasks - 'show'
2. Add task - 'add Your Task'
3. Update task - 'update ID Your new task'
4. Delete task - 'delete ID'
5. Exit program - 'exit'
"""


def get_parser():
    # Argument Parser - commands for cli interaction
    parser = argparse.ArgumentParser(description="Task Tracker CLI app")
    parser.add_argument("action", choices=["add", "update", "delete", "done","progress", "list-all", "list-done"], help="Akce s úkoly")
    parser.add_argument("id", nargs="?", help="ID úkolu")
    parser.add_argument("value", nargs="?", help="Popis úkolu nebo nový úkol")
    return parser