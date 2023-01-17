class Root:
    def pong(self):
        print(f"pong() in Root")
class A(Root):
    def pong(self):
        print(f"pong() in A")
        # super().pong() # GOES TO B
class B(Root):
    def pong(self):
        print(f"pong() in B")
class Leaf(A,B):
    def pong(self):
        print(f"pong() in Leaf")
        super().pong() #GOES TO A
l = Leaf()
l.pong()
