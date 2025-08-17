
""" Private public"""

class Account():
    def __init__(self, ac_number,ac_password):
        self.ac_number = ac_number
        self.__ac_password = ac_password

    def reset_password(self):
        print(self.__ac_password)





account1 = Account("123456","abs123")
print(account1.ac_number)

# Private Property publically not allowed
# print(account1.__ac_password)

account1.reset_password()


class Person:
    __name = "Surbhi"

    @staticmethod
    def good_bye():
        print('good bye')

    def __hello(self):
        print('Hello '+self.__name)
    def welcome(self):
        self.__hello()



p1=Person()
# print(p1.__name)
# p1.__hello()
p1.welcome()
p1.good_bye()
