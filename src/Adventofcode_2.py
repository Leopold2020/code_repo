#Oskar Svedlund
#TEINF-20
#2021-12-01
#Sonar sweep
measurements = []
increments = 0
with open("Advent of code/puzzle_01.egen.txt", "r", encoding="utf8") as puzzle_01:
    for line in puzzle_01:
        measurements.append(int(line))

for i in range(0, len(measurements)-2):
    if measurements[i] + measurements[i+1] + measurements[i+2] > measurements[i+1] + measurements[i] + measurements[i-1]:
        increments+=1
        # print(increments)
        value = measurements[i] + measurements[i+1] + measurements[i+2] - measurements[i+1] + measurements[i] + measurements[i-1]
        print(f"Line {line} is {value} larger than the previus")

    if measurements[i] + measurements[i+1] + measurements[i+2] < measurements[i+1] + measurements[i] + measurements[i-1]:
        # print(increments)
        value = measurements[i+1] + measurements[i] + measurements[i-1] - measurements[i] + measurements[i+1] + measurements[i+2]
        print(f"Line {line} is {value} smaller than the previus")
print(increments)



