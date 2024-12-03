from numbers import Number

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
        Checks that whether the self point is a Number
        """
        # Since bool is simply a subsets of Number, the coord also needs to be made sure that its a valid point
        xValid = isinstance(self.x, Number) and not isinstance(self.x, bool)
        yValid = isinstance(self.y, Number) and not isinstance(self.y, bool)
        return xValid and yValid

    def getCoords(self) -> tuple[int | None, int | None]:
        return (self.x, self.y) if self.getValid() else (None, None)

class Polygon():
    def __init__(self):
        self.__tail = None
        self.__pointCount = 0

    def __str__(self) -> str:
        pointsStr = ""
        curr = self.__tail.next
        while True:
            pointsStr += str(curr)
            if (curr == self.__tail):
                break
            curr = curr.next
            pointsStr += " -> "
        return pointsStr
        
    def addPoint(self, coords: tuple[int]):
        newNode = Point(coords[0], coords[1])
        print(newNode.getValid())
        if not self.__tail:
            self.__tail = newNode
            self.__tail.next = self.__tail
        else:
            tempNode = self.__tail.next
            self.__tail.next = newNode
            self.__tail = newNode
            self.__tail.next = tempNode
        self.__pointCount += 1
