#Absolute imports

from package1 import module1

# from package1.module2 import function1
from package2 import module1
#module1.function1()

from package1 import module2

# module2.function1()

# from package2 import class1
# class1()

import package2 as pg2
# pg2.class1()


from package2.subpackage1.module5 import function2

# function2()

import package2 as pg2

# pg2.subpackage1.module5.function2()

from package1.module2 import *
# from package2.subpackage1.module5 import *

function1()
