#!/usr/bin/env python3
"""This module defines one function `schools_by_topic`"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specifc topic"""
    query = {"topics": topic}
    return mongo_collection.find(query)
