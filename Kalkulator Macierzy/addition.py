def add(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print(f"Cannot add matrixes, sizes are incompatible")
    else:
        rows = len(matrix1)
        cols = len(matrix1[0])
        resultMatrix = []
        for row in range(rows):
            resultMatrix.append([])
            for col in range(cols):
                resultMatrix[row].append([])
                resultMatrix[row][col] = matrix1[row][col] + matrix2[row][col]
        return resultMatrix