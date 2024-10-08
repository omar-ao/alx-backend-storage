#!/usr/bin/env python3
"""This module defines `update_topics` function"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name"""
    query = { "name": name }
    value = { "$set": { "topics": topics } }
    mongo_collection.update_many(query, value)
