from models.user import User
from utils.storage import load

def load_users():
    data = load()
    User.all = []
    User.all = [User.from_dict(u) for u in data.get("users", [])]
    return data