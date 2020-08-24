"""
Collect new data into the archive.

Usage:
  archive collect [--help]
  archive collect <key> <value>
  archive collect <key>
"""
from docopt import docopt
from . import db


def run(argv):
    args = docopt(__doc__, argv=argv)

    key = args["<key>"]
    value = args["<value>"]

    if key and value:
        db.set(key, value)
    elif key:
        print(db.get(key))
    else:
        run(["--help"])
