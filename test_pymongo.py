# pip install pymongo
from pymongo import MongoClient

# connect function
def connect():
    client = MongoClient("mongodb://localhost:27017")
    return client

# test connection
def test_connect():
    conn = connect()
    # print(dir(conn))
    #  dir : returns all properties and methods of the obj
    print("database:")
    for db in conn.list_database_names():
        print(db)


# collection check
def test_collection():
    # connect
    conn = connect()
    # choose db
    db = conn['mydb'] # use mydb
    # choose collection
    coll = db['pymongo']
    return coll


def test_insert():
    # collection
    coll = test_collection()

    # 1 insert
    x = coll.insert_one({
        "name": "Hong",
        "address": "seoul"
    }) # new Document _id return

    # result check
    print(x.inserted_id)


def test_insert_many():
    coll = test_collection()

    # many insert -> [] usig list
    xs = coll.insert_many([
        { "name": "Go", "address": "seoul", "method": "insert_many" },
        { "name": "Jan", "method": "insert_many"},
        { "name": "Im", "job": "theif"}
    ])
    # insert_many -> insered_ids
    print(xs.inserted_ids)
    print(len(xs.inserted_ids), "inserted")

from datetime import datetime

def test_update():
    # address == "seoul"
    # method -> update, modified_at -> current time
    coll = test_collection()

    xs = coll.update_many({ "address": "seoul" },  # condition
                          { '$set': {
                              "method": "update",
                              "modified_at": datetime.now()
                          }}
                          )
    print(xs.matched_count, "matched.") # condition that satisfy
    print(xs.modified_count, "updated.") # actually updated

def test_select_by_filter(filter={}, projection={}):
    """
    db.collection.find({ condition }, { projection })
        projection 1:indicate, 0:not
    """
    coll = test_collection()
    docs = coll.find(filter, projection)

    for doc in docs:
        print(doc)


def test_delete_by_filter(filter = {}):
    coll = test_collection()
    xs = coll.delete_many(filter)
    print(xs.deleted_count, "records deleted!")


import re

if __name__ == "__main__":
    # test_connect()
    # test_insert()
    # test_insert_many()
    # test_update()
    # test_select_by_filter(projection={
    #     "name": 1, "address": 1, "_id": 0
    # }) # filter={}, projection={}
    # SELECT * FROM WHERE  LIKE ->
    # filter = re.compile(r"hong")
    # """
    # db.pymongo.find({ "name": /hong/ }, { "name": 1, "_id": 0)
    # """
    # test_select_by_filter({ "name": filter },
    #                       { "name": 1, "_id": 0 })
    #
    # address == "seoul" delete
    # test_delete_by_filter({ "address": "seoul" })
    # db.pymongo.delete({"address": "seoul"})
    # entire doc delete
    # db.pymongo.delete({})
    test_delete_by_filter()