import sys
sys.path.append('C:/Users/loy/anaconda3/Lib/site-packages')
import pymongo

def get_connection():
    db_name=None
    try:
        connection_url=pymongo.MongoClient("mongodb://localhost:27017/")
        db_name=connection_url["automation_config"]
        print(db_name)
    except Exception as exception:
        print(exception)
    return db_name

# thêm 1 data mongo
def insert_single(collection_name,query,projection=None):
    collection_data=None
    try:
        db_name=get_connection()
        collection_name=db_name[collection_name]
        collection_data=collection_name.insert_one(query,projection)
        print(collection_data)
    except Exception as exception:
        print(exception)
    
    return collection_data

if __name__=="__main__":
    insert_single("config",({"username":"loy1",'age':24}))


# tìm 1 data mongo
def get_single_data(collection_name,query,projection=None):
    collection_data=None
    try:
        db_name=get_connection()
        collection_name=db_name[collection_name]
        collection_data=collection_name.find_one(query,projection)
        print(collection_data)
    except Exception as exception:
        print(exception)
    
    return collection_data



# update 1 data mongo
def update_single_data(collection_name,query,projection=None):
    collection_data=None
    try:
        db_name=get_connection()
        collection_name=db_name[collection_name]
        collection_data=collection_name.update_one(query,projection)
        print(collection_data)
    except Exception as exception:
        print(exception)
    
    return collection_data

