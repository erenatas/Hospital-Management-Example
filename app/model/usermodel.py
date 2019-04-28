from app.common.db import mongo


class CreateUser(object):
    user = ""

    def create_user(self, username, password):
        print(self.user, username)
        user = [{'Type': self.user, '_id': username, 'Password': password}]
        doc = mongo.db.user.insert(user)
        print(doc)
        return self.user, username, password


class Admin(CreateUser):
    user = "0"


class Doctor(CreateUser):
    user = "1"


class Patient(CreateUser):
    user = "2"


class CreateUserFactory:
    @staticmethod
    def user(typ):
        target_class = typ.capitalize()
        return globals()[target_class]()


def find_user(info):
    return mongo.db.user.find_one(info)
