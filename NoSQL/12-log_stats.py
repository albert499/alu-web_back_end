#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient
import sys


def main():
    """Main function to display Nginx log statistics"""
    try:
        client = MongoClient()
        collection = client.logs.nginx

        # Total logs
        total = collection.count_documents({})
        sys.stdout.write("{} logs\n".format(total))

        # Methods
        sys.stdout.write("Methods:\n")
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for method in methods:
            count = collection.count_documents({"method": method})
            sys.stdout.write("\tmethod {}: {}\n".format(method, count))

        # Status check
        status_count = collection.count_documents({"method": "GET", "path": "/status"})
        sys.stdout.write("{} status check\n".format(status_count))
        
        sys.stdout.flush()
    except Exception as e:
        sys.stderr.write("Error: {}\n".format(str(e)))
        sys.exit(1)


if __name__ == "__main__":
    main()
