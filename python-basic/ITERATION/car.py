class Car():
    def __init__(self, engine, doors, color, style, wheels=4):
        self.wheels = wheels
        self.engine = engine
        self.doors = doors
        self.color = color
        self.style = style
        
    def changeDoors(self, doors):
        self.doors = doors
    
    def reconstruct(self, newDoors, newColor, newStyle):
        self.doors = newDoors
        self.color = newColor
        self.style = newStyle
    def getAllProperties(self):
        print('Wheels: ',self.wheels)
        print(self.engine)
        print(self.doors)
        print(self.color)
        print(self.style)
        

car_obj = Car('diesel', 4, 'red', 'bmw')
car_obj.getAllProperties()