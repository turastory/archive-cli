import pickledb
from pathlib import Path


basedir = Path.home() / ".archivedata"
if not basedir.exists():
    basedir.mkdir(exist_ok=True)
    print("Created {str(basedir)} for storing data.")


db = pickledb.load(location=str(basedir / "archive.db"),
                    auto_dump=True)


def get(key):
    value = db.get(key)
    if value:
        return value
    else:
        return None


def get_list(key):
    list = get(key)
    if list: return list
    else: return []


def set(key, value):
    return db.set(key, value)


def lcreate(name):
    return db.lcreate(name)


def ladd(name, key):
    return db.ladd(name, key)
