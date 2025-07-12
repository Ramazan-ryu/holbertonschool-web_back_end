#!/usr/bin/env python3
'''inserts a new document in a collection based on kwargs:
Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id'''
"""pymongo"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection
    based on kwargs
    Args:
    mongo_collection (object): pymongo collection object
    """
    pymongo =  mongo_collection.insertone(kwargs)
    return pymongo.inserted_id
