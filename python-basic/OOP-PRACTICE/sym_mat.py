class SymMatrix:
    def __init__(self, components):
        self.length = len(components)
        isSymetric = (any(len(row) != self.length for row in components))
        self.components = components
        

(1,2) + 1
