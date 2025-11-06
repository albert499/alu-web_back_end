#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """
    Connects to a MongoDB database, retrieves stats from the 'nginx' collection
    in the 'logs' database, and prints them in a specific format.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f"\tMETHOD {method}: {count}")

    status_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_count} status check")

    client.close()

if __name__ == "__main__":
    log_stats()

