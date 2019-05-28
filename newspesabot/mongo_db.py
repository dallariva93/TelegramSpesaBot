import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.binary import STANDARD


class MongoDB:

    _initialized_ = False
    _uri_ = None
    _basic_uri_ = None

    @classmethod
    def init(cls):
        if MongoDB._initialized_:
            return

        MongoDB._initialized_ = True
        MongoDB._init_defaults()

    @classmethod
    def _init_defaults(cls):
        import bson.codec_options
        options = bson.codec_options.DEFAULT_CODEC_OPTIONS \
            .with_options(uuid_representation=STANDARD)
        bson.codec_options.DEFAULT_CODEC_OPTIONS = options

    @classmethod
    def uri(cls) -> str:
        if MongoDB._uri_ is not None:
            return MongoDB._uri_
        MongoDB._uri_ = os.environ['MONGO_URI']
        return MongoDB._uri_


    @classmethod
    def connect(cls) -> MongoClient:
        MongoDB.init()
        uri = MongoDB.uri()
        client = MongoClient(uri)
        return MongoDB.check(client)

    @classmethod
    def check(cls, client: MongoClient) -> MongoClient:
        try:
            # The ismaster command is cheap and does not require auth.
            client.admin.command('ismaster')

        except ConnectionFailure as ex:
            print("mongoDB Server not available: uri: %s -- ex: %s" %
                  (MongoDB.uri, ex))
            raise
        return client

