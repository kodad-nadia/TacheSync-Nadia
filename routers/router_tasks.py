import uuid
from fastapi import APIRouter, HTTPException
from classes.schema_dto import Task, TaskNoID

router = APIRouter(tags=["Tasks"])

tasks = [
    Task(id=str(uuid.uuid4()), name="Task 1", description="Description of Task 1", completed=False),
    Task(id=str(uuid.uuid4()), name="Task 2", description="Description of Task 2", completed=True),
    Task(id=str(uuid.uuid4()), name="Task 3", description="Description of Task 3", completed=False)
]

@router.get('/todos')
async def list_tasks():
    return tasks

@router.post('/todos')
async def create_task(task: TaskNoID):
    new_task = Task(id=str(uuid.uuid4()), **task.dict())
    tasks.append(new_task)
    return new_task

@router.get('/todos/{task_id}')
async def get_task(task_id: str):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put('/todos/{task_id}')
async def update_task(task_id: str, updated_task: TaskNoID):
    for task in tasks:
        if task.id == task_id:
            task.name = updated_task.name
            task.description = updated_task.description
            task.completed = updated_task.completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete('/todos/{task_id}', status_code=204)
async def delete_task(task_id: str):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return
    raise HTTPException(status_code=404, detail="Task not found")


