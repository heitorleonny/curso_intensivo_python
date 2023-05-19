from user import User
from privilleges import Privilleges




class Admin(User):
    def __init__(self, first_name, last_name, sex, age):
        super(Admin, self).__init__(first_name, last_name, sex, age)
        self.privilleges = Privilleges()