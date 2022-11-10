## lists vs. dict
import math

a = 'tr'

d = {'person1': {'name': 'piet', 'job': 'teacher', 'age': 36}, 'person2': {'name': 'chris', 'age': 47}} ##Dictionary are key value pairs
l = ['bla', 'blup'] ## List

# print(l[0])
ages = []
for person in d.values():
    ages.append(person['age'])
    
d2 = {'person1': 1, 'person1':2, 'person2': 3}    
print(d2)

print(d2.items())

for k, v in d2.items():
    print(k, v)

l = ['ele1', 'ele2']

el1, el2 = l

print(el1, el2)