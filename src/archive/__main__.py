"""
Your personal data & knowledge archive.

Usage:
  archive [--version] [--help]
  archive <command> [<args>...]

Option:
  -h --help  Show this screen.
  --version  Show the version

Commands:
  project    Manage projects
  collect    Collect new data for archive.
"""
import sys
from docopt import docopt
from . import meta


def handle_args(argv):
    args = docopt(__doc__,
                  version=meta.__version__,
                  options_first=True,
                  argv=argv)

    command = args["<command>"]
    command_argv = [command] + args["<args>"]
    if command == "project":
        from . import archive_project
        archive_project.run(command_argv)
    elif command == "collect":
        from . import archive_collect
        archive_collect.run(command_argv)
    elif command in ["help", None]:
        handle_args(["--help"])
    else:
        exit(f"Unknown command '{command}' for 'archive'")


if __name__ == "__main__":
    handle_args(sys.argv[1:])
