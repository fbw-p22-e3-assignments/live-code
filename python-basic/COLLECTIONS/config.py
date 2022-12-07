import builtins
from collections import ChainMap

pylookup = ChainMap(locals(), globals(), vars(builtins))
#print(pylookup.get('local_x', 'not found'))
#print(pylookup.get('sum'))

#print(vars(builtins))


# print(globals())

def f():
    local_x = 1
    y = 2
    #sum = 1
    pylookup = ChainMap(locals(), vars(builtins))
  
    print(pylookup)
    print(sum([1,2]))
    #1([1,2])
    #print(pylookup['local_x'])

f()


