#Oskar Svedlund
#Teinf-20
#2021-11-30
#Intro till filhantering

if __name__=="__main__":
    f = open("wins.txt", "r", encoding="utf8") 
    print(f.read())
    f.close() #gamla sättet

    with open("wins.txt", "r", encoding="utf8") as wins:
        #olika sätt att läsa upp filen
        #print(wins.read())
        #print(wins.readline())
        #print(wins.readlines())
        #print(wins.read(4))

        for line in wins.readlines():
            print(line)

    with open("inf20.txt", "w", encoding="utf8") as inf20:
        # r - read
        # x - create ,får error om filen finns
        # w - write ,skapar om den om den ej finns
        # a - append ,lägger till i slutet i filen, skapar filen om den ej finns.
        print("Mata in alla elever i Inf20, skriv # om du vill avsluta")
        while True:
            elev = input("Elev:")
            if '#' in elev:
                break
            else:
                inf20.write(f"{elev}\n")

    with open("inf20.txt", "r", encoding="utf8") as inf20:
        print("Elever i INF20")
        for elev in inf20.readlines():
            print(elev, end="")