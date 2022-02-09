#Oskar Svedlund
#TEINF-20
#2021-09-14
#Gissa talet

import random 
n = random.randint(1,20)

print("Talet är mellan 1 och 20")

for i in range(3):
    x = int(input("Gissa talet: "))

    if x == n:
        print("Grattis det är rätt tal!")
        break

    if x > n:
        print("För stort")
    
    if x < n:
        print("För litet")