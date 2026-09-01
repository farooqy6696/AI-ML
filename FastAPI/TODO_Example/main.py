from fastapi import FastAPI
from pydantic import BaseModel
import json
 
app = FastAPI()
 
 
# Data we receive from POST
class Task(BaseModel):
    title: str
    status: str
 
 
@app.get("/")
def home():
    return {"message": "TODO API is working"}
 
 
@app.get("/tasks")
def get_tasks():
 
    with open("TODO/tasks.json", "r") as file:
        tasks = json.load(file)
 
    return tasks
 
 
# POST - Create a new task
@app.post("/tasks")
def create_task(task: Task):
 
    # Read existing tasks
    with open("TODO/tasks.json", "r") as file:
        tasks = json.load(file)
 
    # Create next ID automatically
    new_id = max([item["id"] for item in tasks], default=0) + 1
 
    # Create new task
    new_task = {
        "id": new_id,
        "title": task.title,
        "status": task.status
    }
 
    # Add new task to the list
    tasks.append(new_task)
 
    # Save updated list to JSON
    with open("TODO/tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
 
    return new_task
 
# PUT - Update task status
@app.put("/tasks/{task_id}")
def update_task(task_id: int, status: str):
 
    # Read existing tasks
    with open("TODO/tasks.json", "r") as file:
        tasks = json.load(file)
 
    # Find the task
    for task in tasks:
 
        if task["id"] == task_id:
 
            # Update status
            task["status"] = status
 
            # Save updated tasks
            with open("TODO/tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)
 
            return task
 
    return {"message": "Task not found"}
 
# DELETE - Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
 
    # Read existing tasks
    with open("TODO/tasks.json", "r") as file:
        tasks = json.load(file)
 
    # Find the task
    for task in tasks:
 
        if task["id"] == task_id:
 
            # Remove the task
            tasks.remove(task)
 
            # Save updated tasks
            with open("TODO/tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)
 
            return {"message": "Task deleted successfully"}
 
    return {"message": "Task not found"}
 