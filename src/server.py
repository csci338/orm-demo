from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from models import User, Task
from models.db import session
from sqlalchemy import select


app = FastAPI()


@app.get("/api/tasks")
async def get_tasks():
    query = select(Task).order_by(Task.id)
    tasks = session.scalars(query)

    # You can't just return the query. Instead, you have
    # to convert each SQLAlchemy Object into a JSON object
    return [task.to_dict() for task in tasks]


@app.get("/api/tasks/{task_id}")
async def get_task(task_id: int):
    query = select(Task).where(Task.id == task_id)
    task = session.execute(query).fetchone()
    if task:
        task = task[0]
        return task.to_dict()
    else:
        return JSONResponse(content={"message": "not found"}, status_code=404)
    
app.mount("/", StaticFiles(directory="ui/dist", html=True), name="ui")
