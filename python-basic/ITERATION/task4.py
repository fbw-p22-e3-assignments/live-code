
print("\n---TASK 4--- \n")

a = 101
b = 3
points = 0

while True:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    if a > 100 and a % 2 != 0 and b % 2 != 0 and a % b == 0:
        points += 1
        print("You earned a point!\n")
    else:
        print("You've made a mistake!\n")
        break
print("You gathered ", points, "point(s)!")