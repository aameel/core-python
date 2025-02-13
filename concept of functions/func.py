# def my_function():
#     print("this is my first function")
#
# my_function()
#
# ####
#
# def my_function(fname):
#     print(fname + "Gupta")
#
#
# my_function("Ram")
# my_function("Shyam")
# my_function("Raju")
#
#
# def my_function(x):
#     return 5*x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))
#
#
# def sum(a ,b):
#     c= a+b
#     print("sum of a,b is:", c)
#     return c
# sum("helo", b"world")
#
#
# def mul(a,b):
#     c= a+b
#     print("mul of a,b is:",c)
#     return c
# mul(10,20)


for num in range(2, 11):
    print(f"Multiplication Table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


