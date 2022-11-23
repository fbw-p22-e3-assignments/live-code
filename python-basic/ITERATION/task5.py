# Task 5 - only digits

print("\n---TASK 5--- \n")
characters = input("Input your characters: ")
print("")

sum_of_digits = 0

for c in characters:
  if c.isdigit():
      print("Found a digit ", c)
      sum_of_digits += int(c)
  if c == '=':
      print("\nExit after finding '=' sign ")
      break

print("\nSum of digits: ", sum_of_digits)