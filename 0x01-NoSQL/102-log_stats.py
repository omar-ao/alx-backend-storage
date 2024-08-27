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

    print("IPs:")
    ip_count = db.nginx.count_documents({"ip": "172.31.63.67"})
    print("\t172.31.63.67: {}".format(ip_count))
    ip_count = db.nginx.count_documents({"ip": "172.31.2.14"})
    print("\t172.31.2.14: {}".format(ip_count))
    ip_count = db.nginx.count_documents({"ip": "172.31.29.194"})
    print("\t172.31.29.194: {}".format(ip_count))
    ip_count = db.nginx.count_documents({"ip": "69.162.124.230"})
    print("\t69.162.124.230: {}".format(ip_count))
    ip_count = db.nginx.count_documents({"ip": "64.124.26.109"})
    print("\t64.124.26.109: {}".format(ip_count))
    ip_count = db.nginx.count_documents({"ip": "64.62.224.29"})
    print("\t64.62.224.29: {}".format(ip_count))
    ip_count = db.nginx.count_documents({"ip": "34.207.121.61"})
    print("\t34.207.121.61: {}".format(ip_count))
    ip_count = db.nginx.count_documents({"ip": "47.88.100.4"})
    print("\t47.88.100.4: {}".format(ip_count))
    ip_count = db.nginx.count_documents({"ip": "45.249.84.250"})
    print("\t45.249.84.250: {}".format(ip_count))
    ip_count = db.nginx.count_documents({"ip": "216.244.66.228"})
    print("\t216.244.66.228: {}".format(ip_count))
