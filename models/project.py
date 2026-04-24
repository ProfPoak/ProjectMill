from datetime import datetime
from models.task import Task

class Project:
    _id_counter = 0

    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        Project._id_counter += 1
        self.id = Project._id_counter
        self.tasks = []

    @property
    def due_date(self):
        return self._due_date
    
    @due_date.setter
    def due_date(self, value):
        try:
            self._due_date = datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {value}. Please use YYYY-MM-DD")
        
    def __str__(self):
        return f"Project #{self.id} | {self.title} | {self.description} | Due: {self.due_date}"
    
    def __repr__(self):
        return f"Project(id={self.id}, title={self.title}, description={self.description}, due_date={self.due_date})"
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": str(self.due_date),
            "tasks": [task.to_dict() for task in self.tasks]
        }
    
    @classmethod
    def from_dict(cls, data):
        project = cls(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"]
        )
        project.id = data["id"]
        Project._id_counter = max(Project._id_counter, data["id"])
        project.tasks = [Task.from_dict(task) for task in data["tasks"]]
        return project