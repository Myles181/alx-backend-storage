#!/usr/bin/env python3
"""Insert school"""

def insert_school(mongo_collection, **kwargs):
    result = mongo_collection.insert_one(kwargs)
    return result.get('_id')
