#Why do we need function
# dry - principle: "don't repeat yourself"  
# 

## global vs. local variables
## parameters and arguments

#Function definition
def input_sum():
    input1=input('give number')
    input2=input('give number')

    input1 = int(input1)
    input2 = int(input2)

    print(sum([input1, input2]))

# input_sum() # Function call

def f(x, z, *rest, t=0, **keyw_rest):
    """
    x is a parameter in my function f
    """
    print('INSIDE FUN',x, z, rest, t, keyw_rest)

f(1,2,3,4,t=1, o=5, j=9 )

def f2(x):
    print(x**2)    ###Side effect
    return x**2

y = f2(2)

print('OUTSIDE',y)



