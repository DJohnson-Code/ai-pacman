import math


# Vector2: A custom 2D vector class to track positions, directions, and movement
# Used for Pac-Man and ghost movement on the game grid
class Vector2:

    def __init__(self, x=0, y=0):
        # Sets the x and y coordinates of the vector
        # If no values are passed in, defaults to (0, 0)
        self.x = x
        self.y = y
        # Threshold for equality checks (helps avoid float rounding issues)
        self.thresh = 0.000001

    def __add__(self, other):
        # Adds two vectors: (x1, y1) + (x2, y2)
        # Used to move Pac-Man or ghosts in a direction
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # Subtracts two vectors: (x1, y1) - (x2, y2)
        # Used to calculate direction or distance between two positions
        return Vector2(self.x - other.x, self.y - other.y)

    def __truediv__(self, scalar):
        # Divides the vector by a number: (x, y) / scalar
        # Useful for scaling movement down (e.g., averaging, smoothing)
        return Vector2(self.x / scalar, self.y / scalar)

    def __neg__(self):
        # Flips the direction of the vector: -(x, y) becomes (-x, -y)
        # Example: Reversing direction
        return Vector2(-self.x, -self.y)

    def __mul__(self, scalar):
        # Multiplies the vector by a number: (x, y) * scalar
        # Example: Speeding up movement
        return Vector2(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        # Compares two vectors using a small threshold
        # Returns True if their x and y are "close enough"
        # Used to check if Pac-Man and a ghost are in the same tile
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
        return False

    def copy(self):
        # Creates a new vector with the same x and y values
        # Useful when you want a duplicate without affecting the original
        return Vector2(self.x, self.y)

    def __str__(self):
        # Returns the vector as a readable string: "(x, y)"
        # So it prints nicely when you use print(vector)
        return f"({self.x}, {self.y})"

    def magnitudeSquared(self):
        # Returns the squared length (distance from origin) of the vector
        # Faster than actual magnitude since it skips the square root
        return self.x**2 + self.y**2

    def magnitude(self):
        # Returns the exact length (distance from origin) using Pythagoras: √(x² + y²)
        # Useful when you want to know how far apart two vectors are
        return math.sqrt(self.magnitudeSquared())
