# #Arthmatic exception
#
# a = 4
# b = 0
# try:
#     c = a / b
#
# except Exception as e:
#     print(e)
#    # print("check your dividend is zero")
#
#
# type error
#
# try:
#     result = "hello" + 5
# except TypeError:
#     print("error: defferent data type ko add ni kar skte")
#
# value error
# try:
#     num = int("a1")
# except ValueError:
#     print("your value is not convertable into int")
#
# index error
#
# try:
#     my_list = [1, 2, 3]
#     print(my_list[5])
# except IndexError:
#     print("error : list ke valid index ko access kare")
#
# key error
#
# try:
#     my_dict = {"name": "john"}
#     print(my_dict["age"])
# except KeyError:
#     print("error: dictionary me esi key nahi hai")
#
# attribute error
#
# try:
#     num = 10
#     print(num.append(5))
# except AttributeError:
#     print("error : object me yeh attribute nahi hai")
#
# file nit found error
# try:
#     f = open("non_existing_file.txt", "r")
# except FileNotFoundError:
#     print("error: file nahi hai please check file name")
#
# name error
#
# try:
#     print(age)
# except NameError:
#     print("error: variable define nahi hai")
#
# import error
#
# try:
#     import non_existing_model
# except ImportError:
#     print("error: module exist nahi krta")
