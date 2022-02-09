#Oskar Svedlund
#TEINF-20
#2021-09-22
#Strängmetoder eller vafan

from typing import Text

#1
x = input("Skirv in en mening jag ska ta bort mellanslag: ")

x = x.replace(" ", "")
print(x)

#3
y = input("Skirv in en mening jag ska se om det är en palidrom: ")

y = y.replace(" ", "")

if y == y[-1::-1]:
    print("det är en palidrom")

else:
    print("det är inte en palidrom") 

#2
z = input("Skriv in en mening jag ska se om du skriker: ")

if z.isupper() == True:
    print("Sluta skirka")
    

m = input("skirv in en mening, jag ska rätta den: ")

if m[1:1:].isupper() == False:
    print("Du glömde stor bokstav.")

if m[-1:-1:].isalpha() == False:
    print("Du glömde skiljetecken.")

#4
n = input("Skriv in en mening jag gör dom till spongebobmeme: ")

i = 0
for x in n:
    if i%2==0:
        print(x.lower(), end = "")
    else:
        print(x.upper(), end = "")
    i += 1
