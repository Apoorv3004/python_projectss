print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want? S,M or L:")
extra_cheese = input("Do you want extra cheese? Y for yes , N for no:")
BILL = 0
if size == "S":
    BILL = 15
elif size == "M":
    BILL =20
elif size == "L":
    BILL = 25

add_pepperoni = input("Do you want add pepperoni? Y or N:")
if add_pepperoni == "Y":
    if size == "S":
         BILL += 2
    elif size == "M":
         BILL += 3
    elif size == "L":
         BILL += 3

if extra_cheese == "Y":
    BILL += 3
print(f'Your final bill is ${BILL}')