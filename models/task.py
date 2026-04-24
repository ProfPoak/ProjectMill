class Task:
    VALID_STATUSES = ["To Do", "In Progress", "Completed"]
    _id_counter = 0

    def __init__(self, title, assigned_to, status="To Do"):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        Task._id_counter += 1
        self.id = Task._id_counter

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if value not in Task.VALID_STATUSES:
            raise ValueError(f"Status must be set to one of the following {Task.VALID_STATUSES}")
        else:
            self._status = value

    @property
    def assigned_to(self):
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("assigned_to must be a non-empty string")
        else:
            self._assigned_to = value

    def __str__(self):
        return f"Task #{self.id} | {self.title} | {self.status} | Assigned to: {self.assigned_to}"

    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status}, assigned_to={self.assigned_to})"