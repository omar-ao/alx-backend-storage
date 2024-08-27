#!/usr/bin/env python3
"""This module contains one function `insert_school`"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """inserts a new document to mongo_collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
