#Oskar Svedlund
#TEINF-20
#2021-09-21
#Svart kung och pi ska visas

print("\u265A")

print("\u03C0")



word = input("skriv in ett ord: ")

if word[1:1:] == word[:-1:-1]:
    print("Det börjar och slutar med samma tecken")

else:
    print("No")


x = "Serieledare"

print(x[:5:1])

print(x[5::1])

print(x[::2])

print(x[:4:3])

print(x[-1::-1])