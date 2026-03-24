from app.database import SessionLocal
from app.models import Task

def test_complete():
    db = SessionLocal()
    task = Task(name="Test", done=False)
    db.add(task)
    db.commit()

    task.done = True
    db.commit()

    assert task.done is True