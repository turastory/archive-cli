import os
from setuptools import setup, find_packages


meta = {}
basedir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(basedir, "src", "archive", "meta.py")) as f:
    exec(f.read(), meta)

setup(
    name="release-tracker",
    version=meta["__version__"],
    description=meta["__description__"],
    author=meta["__author__"],
    author_email=meta["__email__"],
    license=meta["__license__"],
    classifiers=[
        "Topic :: Utilities"
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
)
