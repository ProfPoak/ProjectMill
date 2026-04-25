# ProjectMill

ProjectMill is a CLI project management tool designed to help you churn out your projects. Manage users, projects, and tasks all from the command line.

---

## Setup

**Requirements:**
- Python 3.12
- pipenv

**Installation:**
```bash
git clone <your-repo-url>
cd ProjectMill
pipenv install
pipenv run pip install -e .
```

**Activate the virtual environment:**
```bash
pipenv shell
```

---

## CLI Commands

### Users
```bash
# Add a user
pmill add-user --name "John" --email "john@doe.com"

# List all users
pmill list-users
```

### Projects
```bash
# Add a project (requires a valid user ID)
pmill add-project --title "My Project" --description "A description" --due-date "2026-12-31" --user-id 1

# List all projects
pmill list-projects
```

### Tasks
```bash
# Add a task (requires a valid project ID and existing user name)
pmill add-task --title "My Task" --assigned-to "John" --project-id 1

# List all tasks for a project
pmill list-tasks --project-id 1

# Mark a task as completed
pmill complete-task --task-id 1 --project-id 1
```

---

## Features

- **User management** — add and list users with email validation
- **Project management** — assign projects to users with due date validation
- **Task management** — assign tasks to existing users within projects
- **Status tracking** — tasks support To Do and Completed statuses
- **Data persistence** — all data saved locally to JSON
- **Rich CLI output** — formatted tables with color coded task statuses
- **Full logging** — all commands and errors logged to `data/projectmill.log`

---

## Architecture

ProjectMill is built with extensibility in mind. The `Person` base class allows for future user types such as `Admin` or `Guest` to be added without restructuring the core data model.

```
models/     — User, Project, Task class definitions
utils/      — storage, display, and helper functions
data/       — local JSON database and log file
tests/      — pytest unit tests for models and storage
```

---

## Known Issues & Future Enhancements

- Tasks can only be marked as Completed via `complete-task`. A future `update-task` command would allow status to be set to any valid value.
- No reverse lookup from User to their assigned tasks. A future `list-user-tasks --user-id` command would surface all tasks assigned to a specific user.
- No delete commands currently implemented. Future versions would support `delete-user`, `delete-project`, and `delete-task`.
