import pytest
from models.user import User
from models.project import Project
from models.task import Task

@pytest.fixture
def sample_user():
    return User(name="John", email="john@doe.com")

def test_user_has_name(sample_user):
    assert sample_user.name == "John"

def test_user_has_email(sample_user):
    assert sample_user.email == "john@doe.com"

def test_user_has_id(sample_user):
    assert sample_user.id is not None

def test_two_users_have_unique_id(sample_user):
    user_two = User(name="Jane", email="jane@doe.com")
    assert sample_user.id != user_two.id

def test_user_has_empty_projects_list(sample_user):
    assert sample_user.projects == []

def test_user_str_is_readable(sample_user):
    result = str(sample_user)
    assert "John" in result
    assert "john@doe.com" in result