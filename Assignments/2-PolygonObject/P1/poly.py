"""
Ayaan Khan
735229
Assignment: Polygon Object (P1)
File: poly.py
Purpose: Create a basic polygon class that uses a linked list to manage points
To be extended in another assignment
"""

class Point():
    def __init__(self, x = None, y = None):
        """
        Initializes the current Point
        x, y (int) The x and y coordinates of the current point, given by user

        self.x, self.y (int)        Ditto, stored within Point() itself
        self.next (None | Point)    The next point in the Linked List
        """
        self.x = x
        self.y = y
        self.next = None

    def __str__(self) -> str:
        """
        Returns the self point as a string if the current Point data is valid, otherwise an error message
        Expected pre-req: self.x and self.y are filled out
        """
        return f'({self.x}, {self.y})' if self.getValid() else "Invalid point data"
    
    def getValid(self) -> bool:
        """
        Checks that whether the self point is a int | float
        No pre-req, since this only checks whether its valid
        """
        # Since bool is simply a subsets of Number, the coord also needs to be made sure that its a valid point
        xValid = (isinstance(self.x, int) or isinstance(self.x, float)) and not isinstance(self.x, bool)
        yValid = (isinstance(self.y, int) or isinstance(self.y, float)) and not isinstance(self.y, bool)
        return xValid and yValid

    def getCoords(self) -> tuple[int | float | None, int | float | None]:
        return (self.x, self.y) if self.getValid() else (None, None)

class Polygon():
    def __init__(self):
        self.__tail = None

    def __str__(self) -> str:
        """
        Takes the points of a polygon class and outputs them
        pointsStr (str) The final string
        curr (Point) The current Point to be looked at
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
        
    def addPoint(self, x: int | float, y: int | float):
        """
        Adds a point to the polygon object
        x, y (int|float) The x and y coordinates to add as a point
        
        newNode (Point) A Point created from the x and y coords
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
