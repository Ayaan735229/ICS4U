"""
Ayaan Khan
735229
Assignment: Polygon Object (P1)
File: poly.py
Purpose: Get input from a file and use the within to generate points for the Polygon class
"""

from poly import Polygon

def readFile(filePath = "a2.txt") -> list[str]:
    """
    Takes in a filePath and returns the next as a list
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
    # This shouldn't be necessary, since a context handler is being used, but keeping for safety
    except EOFError as e:
        print("EOFError:", e)
    # Regardless of what happens, return lines
    finally:
        return lines

def convertNumeric(pointStr: str) -> tuple[int|float, int|float]:
    """
    Takes in a point as a string and returns it as a tuple of integer or float
    pointStr (str) The string representing the current point
    
    xStr, yStr (str) Ditto, but split into their x and y
    xPoint, yPoint (int|float) Ditto but converted to int or float
    """
    # Split the pointStr into x and yStr
    xStr, yStr = pointStr.strip("()").split(",")
    # Try to convert to integer
    try:
        xCoord = int(xStr)
    # If it doesn't work, convert to float
    except:
        xCoord = float(xStr)
    # Same for y coord
    try:
        yCoord = int(yStr)
    except:
        yCoord = float(yStr)
    
    
    return (xCoord, yCoord)

def getPointsNumeric(pointsStr: str) -> list[tuple[int|float]]:
    pointStrArr = pointsStr.strip().split(", ")
    pointsArr = []
    for pointStr in pointStrArr:
        pointsArr.append(convertNumeric(pointStr))
    return pointsArr

if __name__ == "__main__":
    fileText = readFile()
    pointsNumeric = getPointsNumeric(fileText[0])
    p = Polygon()

    for x, y in pointsNumeric:
        p.addPoint(x, y)

    print(p)
    
