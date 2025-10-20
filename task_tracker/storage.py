import json
import datetime
from models import Task


def save_data(path, tasks):
    """Saving tasks to JSON file."""
    
    with open(path, "w") as f:
        data = [task.__dict__ for task in tasks]
        json.dump(data, f, default=str, indent=4)
        
        
def load_data(path):
    """Loading data from JSON file."""
    
    try:
        with open(path, "r") as f:
            items = json.load(f)
            data_tasks = [Task(id=item["id"], description=item["description"], status=item["status"]) for item in items]
            for task, item in zip(data_tasks, items):
                task.created_at = datetime.fromisoformat(item["created_at"])
                task.updated_at = datetime.fromisoformat(item["updated_at"])
            return data_tasks
    
    except FileNotFoundError:
        print("File does not exist. Returning empty task list.")
        return []