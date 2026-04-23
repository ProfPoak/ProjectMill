import pytest
from datetime import date
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

@pytest.fixture
def sample_project():
    return Project(title="identify John", description="Contact potential family/acquaintances", due_date="2026-04-25")

def test_project_has_title(sample_project):
    assert sample_project.title == "identify John"

def test_project_has_description(sample_project):
    assert sample_project.description == "Contact potential family/acquaintances"

def test_project_has_due_date(sample_project):
    assert sample_project.due_date is not None

def test_project_due_date_is_date_object(sample_project):
    assert isinstance(sample_project.due_date, date)

def test_project_invalid_due_date_raises_error():
    with pytest.raises(ValueError):
        Project(title="identify John", description="Contact potential family/acquaintances", due_date="NOT-A-DATE")

def test_project_has_id(sample_project):
    assert sample_project.id is not None

def test_two_projects_have_unique_id(sample_project):
    project_two = Project(title="identify Jane", description="Contact potential family/acquaintances", due_date="2026-04-25")
    assert sample_project.id != project_two.id

def test_project_has_empty_task_list(sample_project):
    assert sample_project.tasks == []

def test_project_str_is_readable(sample_project):
    result = str(sample_project)
    assert "identify John" in result
    assert "Contact potential family/acquaintances" in result
    assert str(sample_project.due_date) in result

