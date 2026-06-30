import random
user_choice = int(input("What do you choose? type 0 for Rock, 1 for scissors, 2 for paper"))
computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == user_choice:
    print("It\'s a draw!")
elif computer_choice > user_choice:
    print("You lose!")
else:
    print("You typed a invalid number")
