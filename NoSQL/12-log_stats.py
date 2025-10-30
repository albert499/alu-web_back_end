#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Total number of logs
    total = logs_collection.count_documents({})
    print("{} logs".format(total))

    # Methods statistics
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Status check count
    status = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))
