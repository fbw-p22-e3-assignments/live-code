l = [1,2,3]

### append() add a new element at the end of a list

# l.append([4,5])   ### l is changed in place

# print('line7',l)
l3 = l + l
# print(l3)

l2 = ['x', 'b', 'c', ['a', 'x']]

l.extend(l2)  ### l is extended by l2 in place

#l = l + l2  ### extend occurs not in place

# print(l2[-1])
inner_list = l2[-1]

# inner_list.remove('b')

# print(inner_list)
# print(l2)

# for ele in l2:
#     if 'x' in ele:
#         print('yes x is in my list')


# l2.remove() ## remove inplace 'b' from list l2

# print(l2)

# ele = 'a'

# if ele in l2:
#     l2.remove(ele)
#     print(l2)
# else:
#     print('not in l2')


l2 = ['x', 'b', 'c']

# l2.pop(1)  # ['x', 'c']
# l2.pop(1)  # ['x']

# print(l2)

# l3 = l2.remove('x')

# print('l3', l3)  ## None, because remove only changes inplace
# print('l2', l2)  ## result of inplace change

l2 = ['x', 'b', 'c']
l3 = l2.pop(0)

# print('l3', l3)  ## returns the popped out element
# print('l2', l2)  ## at the same time an inplace change takes place

mylist = ['1', '2', '3']

my_int_list = []

for ele in mylist:
    my_int_list.append([int(ele)])
    print(my_int_list)




