from models.user import User
from utils.storage import load, save

def load_users():
    data = load()
    User.all = []
    User.all = [User.from_dict(u) for u in data.get("users", [])]
    return data

def save_users(data):
    data["users"] = [u.to_dict() for u in User.all]
    save(data)

def find_project(project_id):
    for user in User.all:
        for project in user.projects:
            if project.id == project_id:
                return project
    return None