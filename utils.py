import math 
def palindrome_func(val):
    if not isinstance(val, str):
         val = str(val)
    if val[::-1] == val:
        return True
    else:
        return False

class Circle:
    """
    Features of a circle 
    """
    def __init__(self,radius: float = 1):
        """
        Args:
            radius (float, optional): _description_. Defaults to 1.
        """
        self.radius = radius
        
    def area(self) -> float:
        """

        Returns area of a circle:
            float: _description_
        """
        ar = self.radius**2*math.pi
        return ar
    
    def perimeter(self) -> float:
        """

        Returns perimeter of a circle:
            float: _description_
        """
        perimeter = 2*self.radius*math.pi
        return perimeter
    
    