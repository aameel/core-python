# # # class Person:
# # #     count = 0
# # #
# # #     def __init__(self):
# # #         self.name = ""
# # #         Person.count += 1
# # #
# # #     def setName(self, n):
# # #         self.name = n
# # #
# # #     def getName(self):
# # #        return self.name
# # #
# # # p1 = Person()
# # # p1.setName("ram")
# # # p2 = Person()
# # # p2.setName("shyam")
# # #
# # # print(p1.name)
# # # print(p1.getName())
# # # print(p2.getName())
# # # print(Person.count)
# # from datetime import datetime
# #
# #
# # #################
# #
# # class person:
# #
# #     def __init__(self, name, address, salary):
# #         self.name = name
# #         self.address = address
# #         self.salary = salary
# #
# #     def getname(self):
# #         return self.name
# #
# #     def getaddress(self):
# #         return self.address
# #
# #     def getsalary(self):
# #         return self.salary
# #
# #
# # p1 = person("aameel", "ujjain", 25000)
# # print(p1.getname())
# # print(p1.getsalary())
# # print(p1.getaddress())
# #
# # ##################
# # class account:
# #     def __init__(self, number, accounttype, balance):
# #         self.number = number
# #         self.accounttype = accounttype
# #         self.balance = balance
# #
# #     def getnumber(self):
# #             return self.number
# #
# #     def getaccounttype(self):
# #             return self.accounttype
# #
# #     def getbalance(self):
# #             return self.balance
# #
# #
# # a = account(123425,"saving",30000)
# # print(a.get)
# #
# #
# #
# # ################
#
# class math:
#     def max(a, b):
#         if (a > b):
#             print("result")
#             return a
#         else:
#             return b
#
from idlelib.colorizer import color_config


class automobile:
    def __init__(
        self, color, speed, make):
        self.color = color
        self.speed = speed
        self.make = make

    def getcolor(self):
        return self.color

    def getspeed(self):
        return self.speed

    def getmake(self):
        return self.make

a = automobile("red", 100, "suzuki")
print(a.getcolor())
print(a.getspeed())
print(a.getmake())
