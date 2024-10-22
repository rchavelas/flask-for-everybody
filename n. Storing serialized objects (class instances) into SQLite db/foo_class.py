"""
This file defines the class to be stored later in each database
item as an instance of such class.

As dicussed here: https://stackoverflow.com/questions/69267570/python-sql-storing-objects-or-iterables
other items such as lists (or any python object) can be stored in a
db by serializing the item and storing it as a BLOB, though it is
usually not recommended. 
"""

class Foo:
    def __init__(self):
        self.bar = 0

    def increment(self):
        self.bar += 1
