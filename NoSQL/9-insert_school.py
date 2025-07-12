#!/usr/bin/env python3
'''inserts a new document in a collection based on kwargs:

Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id'''
def insert_school(mongo_collection, **kwargs):
    pymongo =  mongo_collection.insertOne(**kwargs)
    return pymongo.insert_id
