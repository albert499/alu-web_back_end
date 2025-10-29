#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    Provides some stats about Nginx logs stored in MongoDB
    Database: logs
    Collection: nginx
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Get total number of documents
    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))

    # Print Methods header
    print("Methods:")

    # Count documents for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Count status checks (method=GET and path=/status)
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))
