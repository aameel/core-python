import datetime

# x = datetime.datetime.now()
# print(x)

#####
import datetime
x =datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

####

import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

########

import datetime

x = datetime.datetime(2019, 6, 1)
print(x.strftime("%B"))


#############






from datetime import datetime

birth_date = input("Enter your birthdate (YYYY-MM-DD): ")


birth_date = datetime.strptime(birth_date, "%Y-%m-%d")


current_date = datetime.now()


age = current_date.year - birth_date.year


if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
    age -= 1

# Print the age
print("Your age is:", age)

