print("Welcome to the roller coaster?")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")

age = int(input("What is your age?"))
if age <= 12:
    bill= 5
    print("Please pay $5")

elif age <= 18:
    bill = 7
    print("Youth tickets are $7")
elif age >= 45 and age <= 55:
    print("Everything is going to be okay, this ride is on us")

else:
    bill = 12
    print("Adult tickets are $12")
photo_want = input("Would you like to see a photo of you? type y for Yes and n for No")
if photo_want == "y":
     # bill = bill + 3 can be written as shown below
     bill += 3
     print(f'Your bill is: {bill}')

else:
    print("Sorry, you have to grow taller before you can ride the rollercoaster")