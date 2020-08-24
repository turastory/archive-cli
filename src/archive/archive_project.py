"""
Manage projects.

Usage:
  archive project [--help]
  archive project <command> [<name>]

Commands:
  new      Create new project
  list     List all ongoing projects
"""
from docopt import docopt
from . import db


_projects = "__projects"


def create_new_project(project_name):
    if not db.get(_projects):
        db.lcreate(_projects)
    db.ladd(_projects, project_name)


def list_projects():
    return db.get_list(_projects)


def show_help():
    run(["--help"])


def run(argv):
    args = docopt(__doc__, argv=argv)
    command = args["<command>"]

    if command == "new":
        if args["<name>"]:
            create_new_project(args["<name>"])
        else:
            show_help()
    elif command == "list":
        projects = list_projects()
        if projects:
            print("List of projects:")
            for project in list_projects():
                print(f"    {project}")
        else:
            print("No projects found.")
    elif command in ["help", None]:
        show_help()
    else:
        exit(f"Unknown command '{command}' for 'archive project'")
