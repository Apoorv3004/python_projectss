from typing import final

print("Welcome to the tip calculator!")
total = float(input("what was the total bill? $"))
tip = int(input("How much you want to tip?" + "10 or 12 or 15 % ?"))
people = int(input("How many people to split the bill?"))
bill_per_head = (total * (1 + tip / 100)) / people
final_bill_per_head =round(bill_per_head, 2)
print("each person should pay: $ " + str(final_bill_per_head))
