letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("Welcome to the Pypassword Generator")
nr_letters = int(input("How many letters would you like to use in your password? "))
nr_numbers = int(input("How many numbers would you like?\n "))
import random
#easy level
# password = ""
#
# for char in range(0, nr_letters):
#
#     password += random.choice(letters)
#
# for char in range(0, nr_numbers  ):
#     password += random.choice(numbers)
#
# print(password)


#hard level
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)

password= ""
for char in password_list:
    password += char

print(f"Your password is: {password}")