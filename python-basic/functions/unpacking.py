#assign variables
a,b,c = 1,2,3
print(a,b,c)

#swaping a pair of variables
a,b = b, a
b, a = a, b
print(a,b)

#swaping a trio
c, a, b = a, b, c
print(c,a,b)

#spliting string into multiple variables
a, b, c = '4 5 6'.split(' ')
print(a, b, c)

#splitting a list into multiple variables
l = [8, 9, 10]
a, *rest = l
print(a, rest)

#split tuple into variables
tup = (25, 26, 27) #tuples are immutable
x, y, z = tup
print(x,y,z)

#packing multiple variables into one variable
var = x, y, z
print(var)

#*args in Function
def pack_it(*args):
    print(args)
    print(type(args))

x='Hello'
y='World'
z='again' 

pack_it(x, y, z)

#unpacking one argument into multiple parameters
def unpack_it(x, y):
    print(x)
    print(y)

args=('hi', 'again')

unpack_it(*args)
unpack_it('hi', 'again')

#unpack your argument and pack your parameter
def unpack_and_pack_again(*args):
    print(args)

unpack_and_pack_again(*args)

def unpack_and_pack_again(args):
    print(args)

unpack_and_pack_again(args)

#one required positional parameter and unlimited optional parameters
def req1(req, req2, *args):
    print('required', req)
    print('required2', req2)

    print('optional', args)


x='Hello3'
y='World'
z='again' 

req1(x, y, z)

tup = (25, 26, 27) #tuples are immutable

req1(*tup)
req1(25, 26, 27)

#packing multiple variables into one variable
var = x, y, z
print(var)
print(*var)


l1 = [1,2,3]
l2 = [4,5,6]

l3 = [*l1] # [1,2,3]
l3 = [*l1, 'middle', *l2]
l3 = [l1, 'middle', l2]

print(l3)

#**kwargs for Functions
def func(**kwargs):
    print(kwargs)
    if 'optional1' in kwargs.keys():
        value1 = kwargs['optional1']
        print(value1)
    print(type(kwargs))
    
func(a='optional1', b='optional2', c='optional3')

d1 = {'bla1': 'hello', 'bla2': 'world'}
d2 = {'bla3': 'again'}

d3 = { **d1, **d2 } # { 'key1':value1,.....,'keyN':valueN }
# print(1,2,3, sep=' - ', end=' ---END---')
d4 = {'sep': ' - ', 'end': ' ---END--- '}
print(1,2,3, **d4)
print(1,2,3, sep=' - ', end=' ---END---')

func(**d1)


def func(**kwargs):
    print(kwargs.keys())
    if 'a' in kwargs.keys():
        value1 = kwargs['a']
        print(value1)
    print(type(kwargs))


func(a='optional1', b='optional2', c='optional3')

def func(a,b,c):
    print(a)
    print(b)
    print(c)

d1 = {'a': 'hello', 'b': 'world', 'c':'again'}
func(**d1)
func(a='hello', b='world', c='again')

func(*d1.items())
func('hello','world','again')