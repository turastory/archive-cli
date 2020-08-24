"""
Manage projects.

Usage:
  archive project [--help]
  archive project <command> [flags]

Commands:
  new      Create new project
  list     List all ongoing projects
"""
from docopt import docopt


def create_new_project():
    pass


def list_projects():
    pass


def run(argv):
    args = docopt(__doc__, argv=argv)
    command = args["<command>"]

    if command == "new":
        create_new_project()
    elif command == "list":
        list_projects()
    elif command in ["help", None]:
        run(["--help"])
    else:
        exit(f"Unknown command '{command}' for 'archive project'")
