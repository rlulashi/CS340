from pymongo import MongoClient
from bson.objectid import ObjectId
    
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, passwd, host, port, db, collection):
        USER = username
        PASS = passwd
        HOST = host
        PORT = port
        DB = db
        COL = collection
            
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        print("Connection Successful")

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        try:
            if data is not None:
                self.collection.insert_one(data)  # data should be dictionary
                return True
            else:
                raise Exception("Nothing to save, because data parameter is empty")
        except Exception as e:
            print("An exception occurred ::", e)
            return False
    
    # Create Method to implement the R in CRUD.
    def read(self, readdata):
        try:
            if readdata is not None:
                query = self.collection.find(readdata)
                return query
            else:
                return {}
        except Exception as e:
            print("An exception occurred ::", e)
            return {}
    
    # Create Method to implement the U in CRUD
    def update(self, readData, updateData):
        try:
            if readData is not None:
                index_update = self.collection.update(readData, { "$set": updateData })
                return index_update
            else:
                return {}
        except Exception as e:
            print("An exception occurred ::", e)
            return {}
                    
    # Create Method to implement the D in CRUD
    def delete(self, data):
        try:
            if data is not None:
                delete = self.collection.delete_many(data)
                return delete
            else:
                return {}
        except Exception as e:
            print("An exception occurred ::", e)
            return {}
