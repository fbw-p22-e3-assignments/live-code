str1 = 'Hello my name is John'

words = str1.split()

temp = []

for word in words:
    temp.append(word + str(len(word)))

str1_count = ' '.join(temp)
print(str1_count)
