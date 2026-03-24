from app.database import SessionLocal
from app.models import Task

def test_create():
    db = SessionLocal()
    task = Task(name="Test Task")
    db.add(task)
    db.commit()

    result = db.query(Task).filter(Task.name == "Test Task").first()
    assert result is not None