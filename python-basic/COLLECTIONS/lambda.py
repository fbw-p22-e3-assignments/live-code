add15 = lambda x: x +15

print(add15(1))
print(add15(-2))


isOdd = lambda x: x % 2 != 0

isEven = lambda x: x % 2 == 0

getParity = lambda num, parity: isOdd(num) if parity == 'odd' else isEven(num)

print(isOdd(2), isEven(2))
print(isOdd(1), isEven(1))
print(getParity(2, 'odd'), getParity(2, 'even'))
print(getParity(1, 'odd'), getParity(1, 'even'))

starts_with_p = lambda x: x.lower().startswith('p')

print(starts_with_p("Python"))
print(starts_with_p("JavaScript"))
print(starts_with_p("pirate"))


convert = lambda l, num: [num * i for i in l]

numbers = [2, 4, 5, 7, 9, 14]
factor = 2

print(convert(numbers, factor))