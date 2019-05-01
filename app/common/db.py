import pymongo
import sys
import traceback


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance


class MongoConnection(Singleton):
    def __init__(self, db_config):
        # connect db
        try:
            if 'uri' in db_config:
                self.conn = pymongo.MongoClient(db_config['uri'])
                self.db = self.conn[db_config['db_name']]  # connect db
                self.connected = True
            else:
                self.conn = pymongo.MongoClient(db_config['host'], db_config['port'], connect=False)
                self.db = self.conn[db_config['db_name']]  # connect db
                self.username = db_config['username']
                self.password = db_config['password']
                if self.username and self.password:
                    self.connected = self.db.authenticate(self.username, self.password)
                else:
                    self.connected = True
        except Exception:
            traceback.print_exc()
            print('Connect Statics Database Fail.')
            sys.exit(1)

    @staticmethod
    def init_connection(db_config):
        global my_conn
        my_conn = MongoConnection(db_config)

    @staticmethod
    def get_connection():
        global my_connection
        return my_connection

    @staticmethod
    def close_connection():
        global my_connection
        my_connection.close()


MONGODB_CONFIG = {
    'host': '127.0.0.1',
    'port': 27017,
    'db_name': 'hospital',
    'username': None,
    'password': None,
}

my_connection = MongoConnection(MONGODB_CONFIG)
