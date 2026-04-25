from models.person import Person
from models.project import Project

class User(Person):
    _id_counter = 0
    all = []

    def __init__(self, name, email):
        super().__init__(name, email)
        User._id_counter += 1
        self.id = User._id_counter
        self.projects = []
        User.all.append(self)

    def __str__(self):
        return f"User #{self.id} | {self.name} | {self.email}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [project.to_dict() for project in self.projects]
        }
    
    @classmethod
    def from_dict(cls, data):
        user = cls(
            name=data["name"],
            email=data["email"],
        )
        user.id = data["id"]
        User._id_counter = max(User._id_counter, data["id"])
        user.projects = [Project.from_dict(project) for project in data["projects"]]
        return user