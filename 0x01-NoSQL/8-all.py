#!/usr/bin/env python3
"""This module defines one function `list_all`"""
import pymongo


def list_all(mongo_collection):
    """Returns all documents in the `mongo_collection`"""
    docs = mongo_collection.find()
    if docs:
        return docs
    return []
