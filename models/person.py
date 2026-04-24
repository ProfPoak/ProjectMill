from email_validator import validate_email, EmailNotValidError 

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        try:
            validate_email(value)
        except EmailNotValidError:
            raise ValueError("Invalid email address")
        self._email = value

    def __str__(self):
        return f"{self.name} | {self.email}"

    def __repr__(self):
        return f"Person(name={self.name}, email={self.email})"
        