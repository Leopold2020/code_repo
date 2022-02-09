#Oskar Svedlund
#TEINF-20
#2021-09-01
#Moms

print("""
Hallå användare \n 
det här programmet kollar hur mycket en produkt kommer kosta efter moms
""")

x = float(input("Hur mycket kostar produkten?:"))

mons = int(input("Hur många procent mons har produkten? 25, 12 eller 6: ", ))

if(mons == 25):
    y = x * 1,25

elif(mons == 12):
    y = x * 1,12

elif(mons == 6):
    y = x * 1.06
else:
    print("Du behöver välja ett av dom tre procentalternativen, skriv det utan ett % tecken.")


print(f"")