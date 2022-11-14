#### Global SCOPE: 
parameter1 = 1
parameter2 = 2

def funName(parameter1, parameter2):  ##### LOCAL SCOPE
    print(parameter1)                 ##### LOCAL SCOPE

# funName(parameter1, parameter2)


x = 4  ###Global

def f_square_root(x):
    square_root = x ** (1/2)  ###Local variable
    print('INSIDE FUN')   ### side effect
    return square_root    ### return value

# y = f_square_root(x)

z = 10 #Global var

def dummy(bla):   ###call by value, because we are using a immutable datatype
    z = 1
    print('LOCAL', z)
    return z

# dummy(z)   ## HERE I'M calling my fun in GLOBAL SCOPE
# print('GLOBAL',z)

l = [1,2,3]

print(id(l))

def dummy(l):        #call be reference, because we use a mutable datatype  
    l.append(4)
    print('INSIDE',id(l))  #locla l

dummy(l)            # local l will be printed
print('OUTSIDE',l)  #Global l
print(id(l))

CONFIG = {
    'setting_title': 'Hello' 
}

def change_settings(config):
    config['setting_title'] = 'World'    


print(config)

change_settings(CONFIG)

print('after fun call',config)

string1 = 'Hello'
string1[0] = 'W' ##will not work, because strings are immutable

l = list(string1)

l[0] = 'W' # will work, because strings are mutable


