"""
Ayaan Khan
735229
Assignment: Polygon Object (P1)
File: driver.py
Purpose: Get input from a file and use the within to generate points for the Polygon class
To be extended in another assignment
"""

from poly import Polygon

def readFile(filePath = "a2.txt") -> list[str]:
    """
    Takes in a filePath and returns the next as a list
    Pre-req:    The file must exist. Although the absence of one is handled
                its only a simple print of the error,
    filePath (str): The relative or absolute path to the file to be read. Defaults to "a2.txt"
    
    lines (str[]): A list of all the lines in the file
    fh (IO): The handler for whatever file is at filePath
    """
    lines = []
    try:
        # Use a context handler to open the file and add all the lines to lines
        with open(filePath, "r", encoding="utf8") as fh:
            lines = fh.readlines()
    # Handle the file not existing
    except OSError as e:
        print("OSError:", e)
    # Handle the end of the file being reached
    # This shouldn't be necessary, since a context handler is being used, but using just for safety
    except EOFError as e:
        print("EOFError:", e)
    # Regardless of what happens, return lines
    finally:
        return lines

def convertNumeric(pointStr: str) -> tuple[int|float, int|float]:
    """
    Takes in a point as a string and returns it as a tuple of integer or float
    Pre-req: pointStr should be a string in the format of "(x,y)"

    pointStr (str)              The string representing the current point
    
    xStr, yStr (str)            Ditto, but split into their x and y
    xPoint, yPoint (int|float)  Ditto but converted to int or float
    """
    # Split the pointStr into x and yStr
    xStr, yStr = pointStr.strip("()").split(",")
    # Try to convert x to an integer
    try:
        xCoord = int(xStr)
    # If it doesn't work, convert to a float
    except:
        xCoord = float(xStr)
    # Same for y coordinate
    try:
        yCoord = int(yStr)
    except:
        yCoord = float(yStr)
    
    # Return as tuple
    return (xCoord, yCoord)

def getPointsNumeric(pointsStr: str) -> list[tuple[int|float, int|float]]:
    """
    Takes all the points and returns them as a list of tuples, each containing coordinates
    Pre-req: 

    pointsStr (str)             String containing all the points

    pointStrArr (str[])         Array containing all the points as strings, before processing
    pointsArr ((int|float)[])   Array containing all the points as a tuple of integers and/or floats
    pointStr (str)              One of the elements in pointStrArr
    """
    # Convert the string into an array of strings
    pointStrArr = pointsStr.strip().split(", ")
    # Creeate a temporary array, pointsStr
    pointsArr = []
    # For each point string in the array, add them to pointsArr
    for pointStr in pointStrArr:
        pointsArr.append(convertNumeric(pointStr))
    return pointsArr

if __name__ == "__main__":
    # Get the file text
    fileText = readFile()
    # Input the first line, which should have all the points, into getPoints Numeric
    pointsNumeric = getPointsNumeric(fileText[0])
    # Create a new polygon object
    p = Polygon()

    # Add each point into p using the Polygon.addPoint method
    for x, y in pointsNumeric:
        p.addPoint(x, y)

    # Print p
    print(p)
    
