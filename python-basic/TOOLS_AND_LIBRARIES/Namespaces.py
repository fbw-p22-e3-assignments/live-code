import builtins

#print(vars(builtins)['sum'])


# 1. local
# 2. enclosing or nonlocal or free variables 
# 3. global
# 4. built-in
print(sum)
sum = 'my_global'
# print(sum)

def outer():
    X = 2
    sum = 'my_nonlocal'
    # print(locals())
    # print(globals())
    def inner():
        global sum
        #print(sum)
        #del globals()['sum']
        print(sum) # because of LEGB Rule
        #print(sum1)
        sum = 'my_local' #Assignment
    inner()

outer()
print(sum)