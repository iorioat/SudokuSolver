from reader import img2arr
from solver import findSolution
from drawer import solvedImage
from sys import argv

if(argv):
    puzzleMatrix, img = img2arr(argv[1])
    print("\nUnsolved puzzle:\n", puzzleMatrix)

    solvedMatrix = findSolution(puzzleMatrix)
    print("\nSolved puzzle:\n", solvedMatrix)

    solvedImage(img, solvedMatrix)
else:
    print("Invalid input image.")