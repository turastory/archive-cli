"""
Collect new data into the archive.

Usage:
  archive collect [--help]
  archive collect <key> <value>
"""
from docopt import docopt


def collect(key, value):
    pass


def run(argv):
    args = docopt(__doc__, argv=argv)

    key = args["<key>"]
    value = args["<value>"]

    if key and value:
        collect(key, value)
    else:
        run(["--help"])
