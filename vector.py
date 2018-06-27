
import math


class Vec2:
    def __init__(self, *args):
        if len(args) == 0:  # if there are no arguments, init 0,0
            self.x = 0.0
            self.y = 0.0
        elif len(args) == 1: # if there's one argument, it should be a 2-element iterable
            a = tuple(args[0])
            assert len(a) == 2, "Argument length is not 2"
            self.x = float(a[0])
            self.y = float(a[1])
        elif len(args) == 2: # if there are two arguments, they should be 2 numbers
            x, y = args[0], args[1]
            self.x = float(x)
            self.y = float(y)
        else:
            raise ValueError("Invalid arguments for {}.__init__()".format(self.__class__.__name__))

    def __str__(self):
        return "{}({},{})".format(self.__class__.__name__, str(self.x), str(self.y))
        
    def __getitem__(self, k):
        if k == 0:
            return self.x
        elif k == 1:
            return self.y
        else:
            raise IndexError("Index out of range.")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        else:
            raise TypeError("Operand is not a {} instance".format(self.__class__.__name__))
    
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        else:
            raise TypeError("Operand is not a {} instance".format(self.__class__.__name__))
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Vec2(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Operand is not a {} instance".format(self.__class__.__name__))
    
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Vec2(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Operand is not a {} instance".format(self.__class__.__name__))
        
    def __mul__(self, other):
        scalar = float(other)
        return self.__class__(self.x * scalar, self.y * scalar)
        
    def    __truediv__(self, other):
        scalar = 1.0 / float(other)
        return self * scalar
    
    def __neg__(self):
        return self.__class__(-self.x, -self.y)
    
    def dot(self, other):
        """Returns dot product of 2 vectors."""
        
        if isinstance(other, self.__class__):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Argument is not a {} instance".format(self.__class__.__name__))

    @property
    def length_sq(self):
        """Returns vector's length squared.
        
        More efficient than length, doesn't need to calculate square root.
        """
        
        return self.x**2 + self.y**2
    
    @property    
    def length(self):
        """Returns vector's length (magnitude)"""
    
        return math.sqrt(self.length_sq)
    
    @property
    def normalized(self):
        """Returns normalized vector, leaves source vector intact."""
        
        length = self.length
        return self.__class__(self.x/length, self.y/length)
    
    def normalize(self):
        """Normalizes the vector (turns it into unit vector)."""
    
        length = self.length
        self.x /= length
        self.y /= length

    
    @classmethod
    def FromAngleX(cls, angle):
        """Creates a unit vector from angle bwtween the x-axis and the vector."""
        
        radians = math.radians(angle)
        x = math.cos(radians)
        y = math.sin(radians)
        return cls(x, y)

