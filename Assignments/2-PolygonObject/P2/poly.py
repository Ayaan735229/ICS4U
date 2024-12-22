"""
Ayaan Khan
735229
Assignment: Polygon Object (P1)
File: poly.py
Purpose: Create a basic polygon class that uses a linked list to manage all of its points
To be extended in another assignment
"""
import math
import turtle

class Point():
    """
    A singular point within a Polygon

    x, y (int)          Ditto, stored within Point() itself
    next (None|Point)   The next point in the linked list
    """

    def __init__(self, x: int|float = None, y = int|float = None):
        """
        Initializes the current Point
        x, y (int)  The x and y coordinates of the current point, given by user
        """
        self.x = x
        self.y = y
        self.next = None

    def __str__(self) -> str:
        """
        Returns the self point as a string if the current Point data is valid, otherwise an error message
        Expected pre-req: self.x and self.y are filled out
        """
        if self.getValid():
            return f'({self.x}, {self.y})'
        return "Invalid point data"
    
    def getValid(self) -> bool:
        """
        Checks that whether the self point is a int | float
        Pre-req: None; doesn't expect self.x and self.y to be valid, only checks it

        xValid (bool) Whether self.x is valid
        yValid (bool) Whether self.y is valid
        """
        # Check whether the x and y coordiantes are an integers or flaots
        # Also need to make sure they aren't booleans, as they are considered 
        # numbers and can return a false positive without the extra check
        xValid = (isinstance(self.x, int) or isinstance(self.x, float)) and not isinstance(self.x, bool)
        yValid = (isinstance(self.y, int) or isinstance(self.y, float)) and not isinstance(self.y, bool)
        return xValid and yValid

    def getCoords(self) -> tuple[int | float | None, int | float | None]:
        """
        Returns the coordinates if the self coords are valid, otherwise a None point
        Pre-req:    None; self.x and self.y should be filled, but not necessary as
                    something else will return if that is not the case
        """
        if self.getValid():
            return (self.x, self.y)
        return (None, None)
    
    def distance(self, other: 'Point') -> float|None:
        """
        Returns the distance between this point and another, supplied point.
        other (Point)   A point to check the distance to 
        """
        # a^2 + b^2 = c^2
        # a = (a1-a2), b = (b1-b2)
        if self.getValid():
            return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
        return None
    

class Polygon():
    """
    The entire polygon, with methods to add points and to represent the it as a string

    __tail (Point)  The final point of the list. Convenient, because it allows quick access to the start and end the list.
    __len (int)     A count of the number of points in this Polygon object
    """

    def __init__(self):
        """
        Initializes a Polygon object, no parameters needed
        """
        self.__tail = None
        self.__len = 0

    def __str__(self) -> str:
        """
        Takes the points of a Polygon and outputs them as a connected list
        Pre-req: All the coordinates are valid

        pointsStr (str) The final string
        curr (Point)    The Point currently being looked at
        """
        pointsStr = ""
        
        # Get the head        
        curr = self.__tail.next
        pointsStr += str(curr)
        curr = curr.next
        # Check if we've returned to the head
        while not curr == self.__tail.next:
            # Add an arrow to continue the chain
            pointsStr += " -> "
            # Add the stringified version of the current Point and add it to the string
            pointsStr += str(curr)
            # COntinue to the next point
            curr = curr.next
        return pointsStr
    
    def __len__(self) -> int:
        """
        Returns the number of points currently in this Polygon object  
        """
        return self.__len
        
    def addPoint(self, x: int | float, y: int | float):
        """
        Adds a point to the Polygon object
        Pre-req: The user has gotten the points that they need.

        x, y (int|float)    The x and y coordinates to add as a point
        
        newNode (Point)     A Point created from the x and y coords
        """
        # Create a new point, not yet added to the linked list system
        newNode = Point(x, y)
        # There is no tail yet, there are no points yet
        if not self.__tail:
            # Therefore, make the tail and its next equal newNode
            self.__tail = newNode
            self.__tail.next = self.__tail
        # If there is already a point...
        else:
            # Make newNode's next be the head, since it will be the new end node
            newNode.next = self.__tail.next
            # Change the current tail's next to newNode
            self.__tail.next = newNode
            # Replace the current tail with newNode
            self.__tail = newNode
        self.__len += 1

    def getAngle(self, point: Point):
        """
        Uses the cosine law to determine the angle of the point after the one given
        
        point (Point)   The first point in the triangle. Not the one to check the angle for
        
        A (Point)       The point to check the angle for
        B, C (Point)    The other points in the triangle
        a (float)       Distance between B and C, opposite A
        b (float)       Distance between A and C, opposite B
        c (float)       Distance between A and B, opposite C
        angA (float)    Smallest value of angle A
        """
        # Get all three points
        A = point.next
        B = point
        C = A.next

        # Get all distances opposite to the points
        a = B.distance(C)
        b = A.distance(C)
        c = A.distance(B)
        # cos A = (b^2 + c^2 - a^2) / 2bc
        # Use the cosine law to get the smallest angle value
        angA = math.acos((b**2+c**2-a**2)/(2*b*c))
        return angA

    def checkRegularPolygon(self) -> bool:
        """
        Checks whether this Polygon object represents a geometrically regular polygon.

        curr (Point)    The Point currently being looked at
        mDist (float)   The length that each side should be if this polygon is regular
        cdist (float)   The length of the side from curr to curr.next
        mAng (float)    The size that each angle should be if the polygon is regular
        cAng (float)    The size of the angle at curr.next
        """
        # Grab the initial point, which is the tail
        curr = self.__tail
        # Grab the model side length by grabbing its distance to the next point
        mDist = curr.distance(curr.next)
        mAng = self.getAngle(curr)
        # Loop from the head to the tail
        curr = curr.next
        while (not curr == self.__tail):
            # Compare the distance from curr to curr.next to the model distance
            cDist = curr.distance(curr.next)
            cAng = self.getAngle(curr)
            if not cDist == mDist or cDist is None or not cAng == mAng:
                # If it isn't, end the function early and return False to signify an irregular polygon
                return False
            curr = curr.next

        # If the loop has gone through, then that must mean the polygon is regular
        return True
    
    def perimeter(self) -> float:
        """
        Returns the polygon's perimeter

        isRegular (bool)    Represents whether this polygon is regular
        curr (Point)        The Point currenly being looked at 
        perimeter (float)   The perimeter of the polygon (or the distance from the last to the first point)
        """
        # Check whether the polygon is regular, which is important for deciding which calculation to use
        isRegular = self.checkRegularPolygon()
        # If any of the points are invalid, return 0
        if isRegular == None:
            return 0
        
        # Set the curr to the tail
        curr = self.__tail
        perimeter = curr.distance(curr.next)
        # If the polygon is regular...
        if isRegular:
            # ...multiply the distance from the tail to head by the number of Points and return early
            return perimeter * len(self)

        # Otherwise check the distance from each point to the next and sum them up
        perimeter = curr.distance(curr.next)
        curr = curr.next
        while (not curr == self.__tail):
            perimeter += curr.distance(curr.next)
            curr = curr.next
        return perimeter
    
    def area(self) -> float:
        """
        Returns the area of this Polygon object

        isRegular (bool)    Represents whether this polygon is regular
        curr (Point)        The Point currently being looked at
        model (float)
        """
        isRegular = self.checkRegularPolygon()
        # If any of the points are invalid, return 0
        if isRegular == None:
            return 0
        
        # Set curr the the tail
        curr = self.__tail

        # If the area is regular...
        if isRegular:
            # ... use a formula to get the area
            # Formula: A = (n * s^2) ÷ [4tan(pi ÷ n)]
            # Where n is the number of sides and s is the side length
            model = curr.distance(curr.next)
            area = (len(self) * model**2) / (4*math.tan(math.pi / len(self)))

            return area
        
        # Otherwise, follow the step found at
        # https://www.wikihow.com/Calculate-the-Area-of-a-Polygon#Finding-the-Area-of-Irregular-Polygons
        xByY = curr.x * curr.next.y
        yByX = curr.y * curr.next.x

        curr = curr.next
        while not curr == self.__tail:
            xByY += curr.x * curr.next.y
            yByX += curr.y * curr.next.x
            curr = curr.next

        diff = xByY - yByX
        area = diff/2
        return abs(area)
    
    def plot(self):
        """
        Plots the Polygon using turtle
        """
        t = turtle.Turtle()
        t.hideturtle()
        # turtle.tracer(0, 0)
        t.step = 20
        curr = self.__tail

        x, y = curr.getCoords()
        t.pu()
        t.goto(x * t.step, y * t.step)
        t.pd()
        curr = curr.next
        returned = False
        while not returned:
            x, y = curr.getCoords()
            t.goto(x * t.step, y * t.step)

            if curr == self.__tail:
                returned = True
            
            curr = curr.next
        turtle.done()
