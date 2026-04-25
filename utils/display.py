from rich.console import Console
from rich.table import Table

console = Console()

def print_users(users):
    table = Table(title="Users")
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Name", style="white")
    table.add_column("Email", style="white")

    for user in users:
        table.add_row(str(user.id), user.name, user.email)

    console.print(table)

def print_projects(users):
    table = Table(title="Projects")
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Title", style="white")
    table.add_column("Description", style="white")
    table.add_column("Due Date", style="yellow")
    table.add_column("Owner", style="white")
    table.add_column("Tasks", style="white", justify="center")

    for user in users:
        for project in user.projects:
            table.add_row(
                str(project.id),
                project.title,
                project.description,
                str(project.due_date),
                user.name,
                str(len(project.tasks))
            )

    console.print(table)

def print_tasks(project):
    table = Table(title=f"Tasks for: {project.title}")
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Title", style="white")
    table.add_column("Status", style="white")
    table.add_column("Assigned To", style="white")

    for task in project.tasks:
        status_color = "green" if task.status == "Completed" else "yellow" if task.status == "In Progress" else "white"
        table.add_row(
            str(task.id),
            task.title,
            f"[{status_color}]{task.status}[/{status_color}]",
            task.assigned_to
        )

    console.print(table)

def success(message):
    console.print(f"[green]✓ {message} [/green]")

def error(message):
    console.print(f"[red]✗ {message} [/red]")