import time
import pymongo

TIMEOUT = 604800  # one week


class DataHandler:

    @classmethod
    def insert_element(cls, user_id: str, obj: str, collection):
        last_update = time.time()
        key = {"user_id": user_id}
        collection.update_one(key, {'$addToSet': {"list": {"name": obj, "delete_date": last_update + TIMEOUT}}}, upsert=True)
        collection.insert_one(key, {"last_update": last_update})
        # cls.delete_timed_out_elements(key, collection)

    @classmethod
    def delete_timed_out_elements(cls, key: dict, collection):
        collection.update({key,  {'$pull': {"list.delete_date": {'$lt': time.time()}}}})

    @classmethod
    def get_elements(cls, user_id: str, collection) -> list:
        document = collection.find_one({"user_id": user_id})
        return document['list']

    @classmethod
    def delete_timed_out_documents(cls):
        pass





