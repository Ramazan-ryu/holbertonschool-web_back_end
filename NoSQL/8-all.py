#!/usr/bin/env python3
'''// lists all documents in a collection:
// Prototype: def list_all(mongo_collection):
// Return an empty list if no document in the collection
// mongo_collection will be the pymongo collection object'''
"PYMONGO"
def list_all(mongo_collection):
    """List all documents in a collection

    Args:
        mongo_collection (object):
        pymongo collection object
    """
    pymongo = list(mongo_collection.find())
    return pymongo
