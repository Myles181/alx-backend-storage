#!/usr/bin/env python3

def schools_by_topic(school_collection, topic):
    school_data = school_collection.find(
            {'tables': {
                '$elematch': {'$eq': topic}
            }}
        )
    return [data for data in school_data]
