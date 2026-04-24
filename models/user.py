from models.person import Person

class User(Person):
    _id_counter = 0

    def __init__(self, name, email):
        super().__init__(name, email)
        User._id_counter += 1
        self.id = User._id_counter
        self.projects = []