class Root:

    def pong(self):
        print(f"pong() in ROOT")

class A(Root):
    def pong(self):
        print(f"pong() in A")
        super().pong()

class B(Root):
    def pong(self):
        print(f"pong() in B")

class Leaf(A,B):    
    def pong(self):
        print(f"pong() in LEAF")
        super().pong()

l = Leaf()
l.pong()

print(Leaf.__mro__)



