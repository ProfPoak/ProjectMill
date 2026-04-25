import argparse
from models.user import User
from models.project import Project
from models.task import Task
from utils.helpers import load_users, save_users, find_project
import logging

logger= logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(
        prog="pmill",
        description="ProjectMill - CLI project management tool"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # add-user
    add_user_parser = subparsers.add_parser("add-user", help="Add a new user")
    add_user_parser.add_argument("--name", required=True, help="User's name")
    add_user_parser.add_argument("--email", required=True, help="User's email")

    #list-users
    subparsers.add_parser("list-users", help="List all users")

    #add-project
    add_project_parser = subparsers.add_parser("add-project", help="Add a new project")
    add_project_parser.add_argument("--title", required=True, help="Project title")
    add_project_parser.add_argument("--description", required=True, help="Project description")
    add_project_parser.add_argument("--due-date", required=True, help="Due date (YYYY-MM-DD)")
    add_project_parser.add_argument("--user-id", required=True, type=int, help="ID of the user to assign project to")

    #list-projects
    subparsers.add_parser("list-projects", help="List all projects")

    #add-task
    add_task_parser = subparsers.add_parser("add-task", help="Add a new task")
    add_task_parser.add_argument("--title", required=True, help="Task Title")
    add_task_parser.add_argument("--assigned-to", required=True, help="Name of user to assign task to")
    add_task_parser.add_argument("--project-id", required=True, type=int, help="ID of the project to add task to")

    #list-tasks
    list_tasks_parser = subparsers.add_parser("list-tasks", help="List all tasks for a project")
    list_tasks_parser.add_argument("--project-id", required=True, type=int, help="Id of the project")

    # complete-task
    complete_task_parser = subparsers.add_parser("complete-task", help="Mark a task as completed")
    complete_task_parser.add_argument("--task-id", required=True, type=int, help="ID of the task to complete")
    complete_task_parser.add_argument("--project-id", required=True, type=int, help="ID of the project the task belongs to")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()

    elif args.command == "add-user":
        logger.info("add-user command called")
        data = load_users()
        try:
            user = User(name=args.name, email=args.email)
            save_users(data)
            logger.info(f"User created: #{user.id} {user.name} ({user.email})")
            print(f"User '{user.name}' added successfully! (ID: {user.id})")
        except ValueError as e:
            logger.error(f"Failed to create user: {e}")
            print(f"Error: {e}")

    elif args.command == "list-users":
        logger.info("list-users command called")
        data = load_users()
        for user in User.all:
            print(user)
        logger.info("Successfully listed users")

    elif args.command == "add-project":
        logger.info("add-project command called")
        data = load_users()
        user = next((u for u in User.all if u.id == args.user_id), None)
        if user is None:
            logger.error(f"No user found with ID {args.user_id}")
            print(f"Error: No user found with ID {args.user_id}")
            return
        try:
            project = Project(title=args.title, description=args.description, due_date=args.due_date)
            user.projects.append(project)
            save_users(data)
            logger.info(f"Project created: #{project.id} '{project.title}' for user #{args.user_id}")
            print(f"Project '{project.title}' successfully added (ID: {project.id})")
        except ValueError as e:
            logger.error(f"Failed to create project: {e}")
            print(f"Error: {e}")

    elif args.command == "list-projects":
        logger.info("list-projects command called")
        data = load_users()
        for user in User.all:
            print(user)
            if user.projects:
                for project in user.projects:
                    print(f"  {project}")
            else:
                print("  No projects")
        logger.info("Successfully listed projects")

    elif args.command == "add-task":
        logger.info("add-task command called")
        data = load_users()
        project = find_project(args.project_id)
        if project is None:
            logger.error(f"No project found with ID {args.project_id}")
            print(f"Error: No project found with ID {args.project_id}")
            return
        user_names = [u.name for u in User.all]
        if args.assigned_to not in user_names:
            logger.error(f"No user found with name '{args.assigned_to}'")
            print(f"Error: No user found with name '{args.assigned_to}'")
            return
        try:
            task = Task(title=args.title, assigned_to=args.assigned_to)
            project.tasks.append(task)
            save_users(data)
            logger.info(f"Task created: #{task.id} '{task.title}' assigned to {args.assigned_to} in project #{args.project_id}")
            print(f"Task '{task.title}' successfully added (ID: {task.id})")
        except ValueError as e:
            logger.error(f"Failed to create task: {e}")
            print(f"Error: {e}")

    elif args.command == "list-tasks":
        logger.info("list-tasks command called")
        data = load_users()
        project = find_project(args.project_id)
        if project is None:
            logger.error(f"No project found with ID {args.project_id}")
            print(f"Error: No project found with ID {args.project_id}")
            return
        for task in project.tasks:
            print(task)
        logger.info(f"Successfully listed tasks for project #{args.project_id}")

    elif args.command == "complete-task":
        logger.info("complete-task command called")
        data = load_users()
        project = find_project(args.project_id)
        if project is None:
            logger.error(f"No project found with ID {args.project_id}")
            print(f"Error: No project found with ID {args.project_id}")
            return
        task = None
        for t in project.tasks:
            if t.id == args.task_id:
                task = t
                break
        if task is None:
            logger.error(f"No task found with ID {args.task_id}")
            print(f"Error: No task found with ID {args.task_id}")
            return
        task.status = "Completed"
        save_users(data)
        logger.info(f"Task #{args.task_id} marked as Completed in project #{args.project_id}")
        print(f"Task '{task.title}' updated to '{task.status}'")
            

if __name__ == "__main__":
    main()