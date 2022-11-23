
print("\n---TASK 3--- \n")

a = int(input("First number: "))
b = int(input("Second number: "))
print("")

if a < b:
    for i in range(a, b):
        if i % 3 == 0:
            print(i, " is divisible by 3.")
    print("\nFinished iterating from", a, " to", b)
elif a > b:
    for i in range(a, b, -1):
        if i % 5 == 0:
            print(i, " is divisible by 5.")
            break
    else:
        print("\nFinished iterating from", b, " to", a)
else:
    print("Nothing to do, both numbers are equal!")


