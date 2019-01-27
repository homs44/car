
# email, password, name, grade .... 

class User:
    def __init__(self, email, password, name, grade):
        self.email = email
        self.password = password
        self.name = name
        self.grade = grade

    def printAll(self):
        print("email : {0}".format(self.email))
        print("name : {0}".format(self.name))
        print("grade : {0}".format(self.grade))


class UserRepository:

    def __init__(self):
        self.users = []
    
    def add(self, user):
        self.users.append(user)
    
    def update(self, user):
        # update
        for savedUser in self.users:
            if(savedUser.email == user.email):
                savedUser.name = user.name
                savedUser.password = user.password
                savedUser.grade = user.grade
                break


    def delete(self, user):
        # delete
        for savedUser in self.users:
            if(savedUser.email == user.email):
                self.users.remove(user)
        
    
    def findByEmail(self, email):
        # find by id 
        # return user
        for savedUser in self.users:
            if(savedUser.email == email):
                return savedUser


userRepository = UserRepository()

user = User("homs44@naver.com", "123456", "jack", 1)

userRepository.add(user)

temp = userRepository.findByEmail("homs44@naver.com")

if temp is not None:
    temp.printAll()
