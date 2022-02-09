#Oskar Svedlund
#TEINF-20
#2021-09-14
#Räkna ut lönen om den ökar med gånger två varje dag


choice = input("vad vill du?: ")


while(choice != "1"):

    if(choice == "2"):
        x = int(input("Hur många dagar vill du räkna?: "))
        y = 0.01
        for i in range(x):
            #print("Dag", i)
            y = y * 2
            #print("Lön", y)
        else:
            print("dag", i, y, "kr") 

    if(choice == "3"):
        to = int(input("Hur mycket pengar vill du ha?: "))
        m = 0.1
        n = 0
        #while(True):
        while (to > m):
            m = m * 2
            n += 1
        else:
            print("Det tar", n, "dagar för att få ", m, "kr")
            

            # m = 0.01
            # for n in range(to):
            #     m = m * 2

            # if(m > to): 
            #     print("det tar", n, "dagar, för att få ", m, "kr") 
            #     break
                    
            

    
    choice = input("vad vill du?: ")