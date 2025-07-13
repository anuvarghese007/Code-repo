def palindrome_func(s):
    #print(type(s))
    if not isinstance(s,str):
        s=str(s)
    if s[::-1] == s:
        return True
    else:
        return False


import math

class Circle:
    """
    Gives the features of a circle
    """

    def __init__(self, radius: float):
        """
        Initialize a circle.
        
        Args:
            radius (float): Radius of the circle.
        """
        self.radius = radius

    def area(self) -> float:
        """
        get the area of the circle
        """
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """
        get the perimeter of the circle
        """
        return 2 * math.pi * self.radius
