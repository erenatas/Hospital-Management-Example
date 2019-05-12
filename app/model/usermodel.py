from app.common.db import my_connection


'''
CreateUser class is for database operations related to users. Currently it contains only one functionality, which is
create_user function. CreateUser class takes advantages of Factory Method pattern. 

Factory Pattern separates the process of creating an object from the code that depends on the interface of the 
object. For example, an application requires an object with a specific interface to perform its tasks. The concrete 
implementation of the interface is identified by some parameter. Instead of using a complex if/elif/else conditional 
structure to determine the concrete implementation, the application delegates that decision to a separate component 
that creates the concrete object. With this approach, the application code is simplified, making it more reusable and 
easier to maintain. 

Here, create_user method is called from CreateUserFactory. CreateUserFactory gets the type of the user that it will
create it's user and then create_user method will be called from there. Usage can be seen in usercontroller.py . 
'''


class CreateUser(object):
    user = ""

    def create_user(self, username, password):
        print(self.user, username)
        user = [{'Type': self.user, '_id': username, 'Password': password}]
        doc = my_connection.db.user.insert(user)
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
    return my_connection.db['user'].find_one(info)


