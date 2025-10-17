from datetime import datetime

class Task:
    def __init__(self, id, description, status="todo"):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def mark_as_done(self):
        self.status = "done"
        self.updated_at = datetime.now()
    
    def mark_as_in_progress(self):
        self.status = "in_progress"
        self.updated_at = datetime.now()
        
    def update_description(self, new_description):
        self.description = new_description
        self.updated_at = datetime.now()
        
    def __str__(self):
        return f"[{self.id}] {self.description} ({self.status})"


class TaskManager():
    def __init__(self):
        self.tasks = []
        self._next_id = 1
        
    def add_task(self, description):
        task = Task(self._next_id, description, status="todo")
        self.tasks.append(task)
        self._next_id += 1
        return task
        
    def update_task(self, id, new_description):
        for task in self.tasks:
            if task.id == id:
                task.update_description(new_description)
                return task
        
        raise ValueError(f"Task with id {id} not found")
        
    def delete_task(self, id):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                return task
            
        raise ValueError(f"Task with id {id} not found")
        
    def mark_task_done(self, id):
        for task in self.tasks:
            if task.id == id:
                task.mark_as_done()
                return task
            
        raise ValueError(f"Task with id {id} not found")
        
    def mark_task_in_progress(self, id):
        for task in self.tasks:
            if task.id == id:
                task.mark_as_in_progress()
                return task
            
        raise ValueError(f"Task with id {id} not found")
        
    def list_all_tasks(self):
        for task in self.tasks:
            print(task)
        
    def list_done_tasks(self):
        for task in self.tasks:
            if task.status == "done":
                print(task)
        
        