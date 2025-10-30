#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient


def main():
    """Main function to display Nginx log statistics"""
    client = MongoClient()
    collection = client.logs.nginx

    # Total logs
    total = collection.count_documents({})
    print("{} logs".format(total))

    # Methods
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Status check
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_count))


if __name__ == "__main__":
    main()
