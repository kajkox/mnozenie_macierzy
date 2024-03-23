from setup import *
from determinant import *
from addition import *

while True:
    print("""
          --------------------
        [0] - exit
        [1] - create an empty matrix
        [2] - write/overwrite a matrix
        [3] - calculate determinant
        [4] - add two matrices
          --------------------
        """)
    ans = str(input("Please select your option:"))
    match ans:
        case '0':
            exit()
        case '1':
            while True:
                newRows = int(input("Please input the amount of rows you would like your matrix to have: "))
                newCols = int(input("Please input the amount of columns you would like your matrix to have: "))
                print(f"Your choice is a {newRows}x{newCols} matrix, correct?")
                choice = str(input("[Y/N]: "))
                if choice.upper() == 'Y':
                    break
                elif choice.upper() == 'N':
                    pass
            createEmptyMatrix(rows=newRows, cols=newCols)
            print("Matrix created and saved successfully")
        case '2':
            printAllMatrices()
            mat = int(input("Please select your matrix of choice: \n"))
            writeInAnEmptyMatrix(listOfMatrices[mat])
            print("Matrix ovverwritten successfully")
        case '3':
            printAllMatrices()
            mat = int(input("Please select your matrix of choice: \n"))
            print("The result is: ", det(listOfMatrices[mat]))
        case '4':
            printAllMatrices()
            mat1 = int(input(f"Please select your first matrix of choice: "))
            mat2 = int(input(f"Please input your second matrix of choice: "))
            print("The result is: \n")
            displaySingleMatrix(add(listOfMatrices[mat1], listOfMatrices[mat2]))
            while True:
                sv = str(input("Do you want to save your result? \n[Y/N]: "))
                if sv.upper() == 'Y':
                    saveAMatrix(add(listOfMatrices[mat1], listOfMatrices[mat2]))
                    print("Result saved succesfully.")
                    break
                elif sv.upper() == 'N':
                    print("Discarding result.")
                    break
                else:
                    print("Please select a correct option.")
                    pass
        case _:
            print("Please select a proper option.")
