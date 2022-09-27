import numpy as np
import cv2
import pytesseract
import sys


def solvedImage(img, solution):
	solution = np.transpose(solution)

	# img = cv2.imread(imgDir, 0)
	# img = cropGameBoard(img)
	# img = cv2.bitwise_not(img)
	cellWidth = int(img.shape[0] / 9)
	cellHeight = int(img.shape[1] / 9)
	img = np.full((img.shape[0], img.shape[1], 1), 255, dtype = "uint8")

	for i in range(9):
		for j in range(9):
			cv2.putText(img, str(solution[i][j]), (int(cellWidth*i+10), int(cellHeight*j+35)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
	
	cv2.line(img, (int(img.shape[0]/3.1),10), (int(img.shape[0]/3.1), img.shape[1]), (0, 255, 0), 4)
	cv2.line(img, (int(img.shape[0]/1.55),10), (int(img.shape[0]/1.55), img.shape[1]), (0, 255, 0), 4)

	cv2.line(img, (10, int(img.shape[0]/3)), (img.shape[0], int(img.shape[0]/3)), (0, 255, 0), 4)
	cv2.line(img, (10, int(img.shape[0]/1.5)), (img.shape[0], int(img.shape[0]/1.5)), (0, 255, 0), 4)

	print("\n--- Press any key (on the popup window) to close ---")
	cv2.imshow("solution", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	sys.exit(0)

