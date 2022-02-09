# Oskar Svedlund
# TEINF-20
# 2021-09-13
# Uppgift att göra loops

x = int(input("Vilket tal ska jag börja på? "))
y = int(input("Vilket tal ska jag räkna till? "))

z = 0
if x > y:
    z = -1
    y -= 1
else:
    z = 1
    y += 1
for i in range (x, y, z):
    print(i)
else:
    print("färdig!")

#To += 1
"""
if From >= To:
    for x in range(From, To):
        print(x)
    else: 
        print("Klar.")    
else:
    for x in range(From, To, -1):
            print(x)        
    else: 
        print("Klar.")

"""