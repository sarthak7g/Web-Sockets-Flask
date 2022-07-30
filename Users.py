from threading import Lock

class Users:
    users = []
    lock = Lock()

    @staticmethod
    def getUsers():
        return Users.users

    @staticmethod
    def getUserById(id):
        return next(filter(lambda u: u['id'] == id, Users.users), None)

    @staticmethod
    def addUser(user):
        Users.lock.acquire()
        Users.users.append(user)
        Users.lock.release()

    @staticmethod
    def removeUser(id):
        Users.lock.acquire()
        Users.users = list(filter(lambda u: u['id'] != id, Users.users))
        Users.lock.release()



if __name__ == '__main__' :
    print(Users.getUsers())
    Users.addUser({'id': 1})
    Users.addUser({'id': 2})
    print(Users.getUsers())
    Users.removeUser(1)
    print(Users.getUsers())
    Users.addUser({'id': 3})
    print(Users.getUserById(5))