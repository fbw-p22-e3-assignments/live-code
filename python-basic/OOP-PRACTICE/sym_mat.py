class SymMatrix:
    def __init__(self, components):
        self.length = len(components)
        isSymetric = all([len(row) == self.length for row in components])
        print(isSymetric)
        if isSymetric:
            self.components = components
        else:
            raise ValueError("Not a symmetric matrix")

    def __str__(self):
         matrix = str("\n".join([ '('+' '.join([str(col) for col in row]) + ')' for row in self.components]))
         return matrix

    def shape(self):
         return (self.length, self.length)

    def __matmul__(self, other):
         if self.shape()[1] != other.shape()[0]:
             raise ValueError("Matrix dimensions do not match")
         else:
             pass
             result = [[str(ele)+'A' for ele in rowX] for rowX in zip(self.components, other.transpose().components)]
             return SymMatrix(result)

    def transpose(self):
        return SymMatrix(list(zip(*self.components)))
    
        

p1 = SymMatrix([[1, 2], [3, 4]])
p2 = SymMatrix([[4, 5], [6, 5]])
print(p1.transpose())
print(p1 @ p2)


