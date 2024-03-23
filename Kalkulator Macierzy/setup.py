def createEmptyMatrix(rows, cols) -> list:
    emptyMatrix = []
    for y in range(rows):
        emptyMatrix.append([])
        for x in range(cols):
            emptyMatrix[y].append([])
    listOfMatrices.append(emptyMatrix)

def writeInAnEmptyMatrix(matrix) -> list:
    rows = len(matrix)
    cols = len(matrix[0])
    for x in range(rows):
        for y in range(cols):
            value = float(input(f"Please input the value for the {y+1} column of the {x+1} row: "))
            matrix[x][y] = value
    return matrix

def printAllMatrices():
    for x in range(len(listOfMatrices)):
        print(f"[{x}] - \n")
        for y in range(len(listOfMatrices[x])):
            print(f"{listOfMatrices[x][y]}\n")

def displaySingleMatrix(matrix):
    for x in range(len(matrix)):
        print(f"{matrix[x]}\n")

def saveAMatrix(matrix):
    listOfMatrices.append(matrix)

listOfMatrices = []