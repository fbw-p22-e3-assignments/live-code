dict1 = {
  'a': 4,
  'b': 16,
  'c': 3
}

dict2 = {
  'a': 8,
  'b': 2,
  'c': 3
} 

sum = 0
for v in zip(dict1.values(), dict2.values()):
    sum += v[0] * v[1]

print(sum)

sum = 0
for k in dict1.keys():
    sum += dict1[k] * dict2[k]

print(sum)

