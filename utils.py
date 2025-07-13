import math 
def palindrome_func(val):
    if not isinstance(val, str):
         val = str(val)
    if val[::-1] == val:
        return True
    else:
        return False

class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        ar = self.radius**2*math.pi
        return ar
    
    def perimeter(self):
        perimeter = 2*self.radius*math.pi
        return perimeter
    
    