#!/usr/bin/env python3
""" Pretty logs in python with Mongo """
from pymongo import MongoClient


def count(mg_col, method):
    """ Writing an simple count function for reducing the repetition """

    res = mg_col.count_documents({"method": method})
    return res

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    ng_collection = client.logs.nginx

    print(f"{ng_collection.count_documents({})} logs")
    print("Methods:")
    for i in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"	method {i}: {count(ng_collection, i)}")
    print("{} status check".format(ng_collection.count_documents({"path": "/status"})))
