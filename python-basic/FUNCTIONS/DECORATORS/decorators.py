def decorate(func):
    func()
    def inner():
        print('runnning inner()')
    return inner

##################### SNIPPET 1#############
@decorate
def target():
    print('running target()')

############################################

##################### SNIPPET 2#############
def target():
    print('running target()')

target = decorate(target)

############################################
#SNIPPET 1 AND SNIPPET 2 ARE EQUAL 