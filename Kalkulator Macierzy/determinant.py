def isSquare(matrix):
    return len(matrix) == len(matrix[0])

def det(matrix):
    if not isSquare(matrix):
        print("Cannot calculate det, matrix possibly not square.")
    else:
        size = len(matrix)
        match size:
            case 1:
                return sizeOne(matrix)
            case 2:
                return sizeTwo(matrix)
            case 3:
                return sizeThree(matrix)
            case _ if size >= 4:
                return laPlasse(matrix)
            case _:
                print("Something went wrong with determining the size of the matrix...")

def sizeOne(matrix):
    return matrix[0][0]

def sizeTwo(matrix):
    positive = matrix[0][0] * matrix[1][1]
    negative = matrix[0][1] * matrix[1][0]
    return positive - negative

def sizeThree(matrix):
    positive = (matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[1][0] * matrix[2][1] * matrix[0][2]) + (matrix[2][0] * matrix[0][1] * matrix[1][2])
    negative = (matrix[0][2] * matrix[1][1] * matrix[2][0]) + (matrix[0][0] * matrix[2][1] * matrix[1][2]) + (matrix[0][1] * matrix[1][0] * matrix[2][2])
    return positive - negative

def laPlasse(matrix):
    size = len(matrix)
    total = 0
    for x in range(size):
        minor = getMinor(matrix, x)
        if x % 2 != 0:
            s = 1
        else:
            s = -1
        total += s * matrix[size-1][x] * det(minor)
    return total

def getMinor(matrix, col):
    size = len(matrix)
    minor = []
    for x in range(0, size-1):
        minor.append([])
        for y in range(size):
            if y == col:
                pass
            else:
                minor[x].append(matrix[x][y])
    return minor

