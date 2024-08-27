#!/usr/bin/env python3
"""This is a python script provides some stats about Nginx logs stored in
MongoDB"""
import pymongo
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient()
    db = client.logs

    get = db.nginx.count_documents({"method": "GET"})
    post = db.nginx.count_documents({"method": "POST"})
    put = db.nginx.count_documents({"method": "PUT"})
    patch = db.nginx.count_documents({"method": "PATCH"})
    delete = db.nginx.count_documents({"method": "DELETE"})
    get_status = db.nginx.count_documents({"method": "GET", "path": "/status"})

    total = db.nginx.count_documents({})

    print("{} logs".format(total))
    print("Methods:")
    print("\tmethod GET: {}".format(get))
    print("\tmethod POST: {}".format(post))
    print("\tmethod PUT: {}".format(put))
    print("\tmethod PATCH: {}".format(patch))
    print("\tmethod DELETE: {}".format(delete))
    print("{} status check".format(get_status))
