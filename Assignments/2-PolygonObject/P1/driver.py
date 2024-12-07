from poly import Polygon

def readFile(filePath = "a2.txt") -> list[str]:
    lines = []
    with open(filePath, "r") as fh:
        lines = fh.readlines()
    return lines

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

def getPointsNumeric(pointsStr: str) -> list[tuple[int|float]]:
    pointStrArr = pointsStr.strip().split(", ")
    pointsArr = []
    for pointStr in pointStrArr:
        pointsArr.append(convertNumeric(pointStr))
    return pointsArr

if __name__ == "main":
    fileText = readFile()
    pointsNumeric = getPointsNumeric(fileText[0])
    p = Polygon()

    for point in pointsNumeric:
        p.addPoint(point)

    print(p)
