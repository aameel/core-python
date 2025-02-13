# from datetime import datetime
#
#
# class Person:
#
#     def __init__(self, name, dob, address):
#         self.name = name
#         self.dob = dob
#         self.address = address
#
#     def getname(self):
#         return self.name
#
#     def getdob(self):
#         current_year = datetime.now().year
#         return current_year - self.dob
#
#     def getaddress(self):
#         return self.address
#
#
# p = Person("aameel", 2002, "ujjain")
# print("name:", p.getname())
# print("dob:", p.getdob())
# print("address:", p.getaddress())
#
#
#
# #
#
# from datetime import datetime
#
#
# class Person:
#     def __init__(self, name, dob, address):
#         self.name = name
#         self.dob = dob  # dob should be a full birth year, e.g., 2002
#         self.address = address
#
#     def getname(self):
#         return self.name
#
#     def getdob(self):
#         current_year = datetime.now().year
#         return current_year - self.dob  # Assuming dob is a birth year (int)
#
#     def getaddress(self):
#         return self.address
#
#
# # Creating an instance with proper birth year
# P = Person("Aniket", 2002, "Indore")
#
# # Printing details
# print("Name:", P.getname())
# print("Age:", P.getdob())  # Now this correctly calculates age
# print("Address:", P.getaddress())
import codecs


#
# class Account:
#     def __init__(self, account_no, account_type, balance):
#         self.account_no = account_no
#         self.account_type = account_type
#         self.balance = balance
#
#     def getAccountNumber(self):
#         return self.account_no
#
#     def getAccountType(self):
#         return self.account_type
#
#     def getBalance(self):
#         return self.balance
#
#     def deposit(self, amount):


# class Automobile:
#
#     def __init__(self, color, speed, make,gear):
#         self.color = color
#         self.speed = speed
#         self.make = make
#         self.gear =gear
#
#     def getcolor(self):
#         return self.color
#
#     def getspeed(self):
#         return self.speed
#
#     def getmake(self):
#         return self.make
#
#     def gear(self):
#         if (self.speed < 1):
#             return 1
#         if (20 < self.speed <= 40):
#             return 2
#         if (40 < self.speed <= 60):
#             return 3
#         if (60 < self.speed <= 80):
#             return 4
#         if (self.speed > 80):
#             return 5
#
#
# p = Automobile("blue", 58, "sauden","gear")
# print("color=",p.getcolor())
# print("speed",p.getspeed())
# print(("make"),p.getmake())
# print("gear",p.getgear())


class Automobile:

    def __init__(self, color, speed, make):
        self.color = color
        self.speed = speed
        self.make = make

    def getcolor(self):
        return self.color

    def getspeed(self):
        return self.speed

    def getmake(self):
        return self.make

    def Gear(self):
        if self.speed < 1:
            return 1
        elif 20 < self.speed <= 40:
            return 2
        elif 40 < self.speed <= 60:
            return 3
        elif 60 < self.speed <= 80:
            return 4
        elif self.speed > 80:
            return 5
        else:
            return "Invalid speed"


C = Automobile("Red", 48, "Sedan")


print("Automobile Details:")
print(f"Color: {C.getcolor()}")
print(f"Speed: {C.getspeed()} km/h")
print(f"Make: {C.getmake()}")
print(f"Current Gear: {C.Gear()}")


