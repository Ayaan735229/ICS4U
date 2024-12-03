from poly import Polygon

def readFile(fileName: str = "a2", fileExt: str = ".txt") -> list[str]:
    lines = []
    with open(fileName + fileExt, "r") as fh:
        lines = fh.readlines()
    return lines

# TODO: find if the try catch blocks can be replaced
def convertNumeric(pointStr: str) -> tuple[int|float]:
    xStr, yStr = pointStr.strip("()").split(",")
    try:
        x = int(xStr)
    except:
        x = float(xStr)
    try:
        y = int(yStr)
    except:
        y = float(yStr)
        
    return (x, y)

# TODO: Make this function not so miserable to read
def getPointsNumeric(pointsStr: str) -> list[tuple[int|float]]:
    pointStrArr = pointsStr.strip().split(", ")
    pointsArr = []
    for pointStr in pointStrArr:
        pointsArr.append(convertNumeric(pointStr))
    return pointsArr
    

fileText = readFile()
pointsNumeric = getPointsNumeric(fileText[0])
p = Polygon()

for point in pointsNumeric:
    p.addPoint(point)

print(p)
