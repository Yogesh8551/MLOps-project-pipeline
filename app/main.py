from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Task, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/task")
def create(name: str, db: Session = Depends(get_db)):
    task = Task(name=name)
    db.add(task)
    db.commit()
    return {"message": "Task created"}

@app.get("/tasks")
def read(db: Session = Depends(get_db)):
    return db.query(Task).all()

@app.put("/task/{task_id}")
def complete(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.done = True
        db.commit()
        return {"message": "Task completed"}
    return {"error": "Task not found"}

import subprocess

@app.get("/run-ml")
def run_ml():
    # simulate change
    with open("changed_files.txt", "w") as f:
        f.write("main.py")

    # run ML script
    subprocess.run(["python", "ml/predict.py"])

    # read output
    with open("tests_to_run.txt") as f:
        tests = f.read().splitlines()

    return {
        "changed_file": "main.py",
        "selected_tests": tests
    }