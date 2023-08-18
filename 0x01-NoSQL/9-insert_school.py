#!/usr/bin/env python3
"""Insert school"""

def insert_school(mongo_collection, **kwargs):
    """Insert more collections into mongo_collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
