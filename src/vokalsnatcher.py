#Oskar Svedlund
#TEINF-20
#2021-09-20
#Vokal snatcher

word = input("Hej användare, skriv in ett ord eller mening: ")

for i in word:
    if i == "a" or i =="e" or i =="u" or i =="o" or i =="i" or i =="y" or i =="å" or i =="ä" or i =="ö":
        continue
    print(word, end=" ")