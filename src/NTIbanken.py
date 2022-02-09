# Oskar Svedlund
# TEINF-20
# 2021-09-07
# NTIbanken

print("""
Hallå använadre det här är NTI banken dina alternativ är /n
1. Visa din saldo
2. Sätt in pengar
3. Ta ut pengar
4. Få spartips
0. När som helst i programmet skriv in 0 för att avsluta programmet
""")

choice = input("Ditt val?:")

money = 400

while(choice != "0"):

    if(choice == "1"):
        print(f"Din saldo är {money} kr")

    elif(choice == "2"):
        num_one = int(input("Hur mycket vill du lägga in: "))
        money += num_one
        print(f"Du har nu {money} kr på kontot")

    elif(choice == "3"):
        num_two = int(input("Hur mycket vill du ta ut: "))
        money -= num_two
        print(f"Du har nu {money} kr kvar på kontot")

    elif(choice == "4"):
        print("Spendera mindre din gubbe")

    elif(choice == "#"):
        print("""
        1. Visa din saldo
        2. Sätt in pengar
        3. Ta ut pengar
        4. Få spartips
        0. När som helst i programmet skriv in 0 för att avsluta programmet
        """)

    elif(choice == "0"):
        break

    else:
        print("det är inte ett alternativ")
    
    print("För att se menyn igen skriv #")
    choice = input("Ditt val: ")




