import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='profilecode',
    version='0.0.1',
    packages=find_packages(include=['profilecode', 'profilecode.*']),
    author="New Hire",
    install_requires=[
       "pytest",
       "pytest-benchmark",
       "Faker",
       "rich",
       "snakeviz",
       "numpy"
    ]
)