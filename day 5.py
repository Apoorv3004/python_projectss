students_score = (150,234,334,213,256,687,211,87,90,67,78,56,345,255)

maxscore = 340
for score in students_score:
    if score > maxscore:
        maxscore += score

print("The highest score is",maxscore)

for number in range(1,101):
    if number %3 ==0:
        print("fizz")
    elif number %5 ==0:
        print("buzz")
    elif number %15==0:
        print("fizzbuzz")
    else:
        print(number)