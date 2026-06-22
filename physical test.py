print("Welcome to our football academy.")
print("You have to provide real data in the upcoming questions. On the basis of your answer we will short list your name.")
height = int(input("What is your height in cm? "))
if height >165:
    print("Your height is perfect for our trial")
else:
    print("You are not in our height criteria but if you are exceptionally good in other category we can consider you in our list")

weight = int(input("What is your weight in kg? "))
if weight >65 or weight <90:
    print("Your weight is perfect for our trial")
else:
    print("either you are too heavy or you are too light")

highest_jump = int(input("What is your highest jump in cm "))
if highest_jump > 210:
    print("Your highest jump is perfect for our trial")
else:
    print("You are not eligible in our crietria")

yoyo_score = float(input("What is your yoyo_score "))
if yoyo_score >15.5:
    print("Your yoyo_score is perfect for our trial")
else:
    print("You are not eligible in our crietria")

fastest_speed = float(input("What is your fastest speed in football boots in kmph"))
if fastest_speed > 22:
    print("Your fastest_speed is perfect for our trial")
else:
    print("You are not eligible in our crietria")
print("if you passed 3 or more than 3 of the criteria you can have a last chance of selection by giving a offline attendence in our academy" + " " + "if you are scoring 5/5 then congratulations you are selected our academy will contact you for trials and confirmation of your data")