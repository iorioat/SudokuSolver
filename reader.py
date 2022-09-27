import numpy as np
import cv2
import pytesseract

zz = np.array([[3,0,0,2,9,0,0,0,7]
              ,[0,7,0,0,0,0,0,8,3]
              ,[0,0,8,0,3,0,9,1,0]
              ,[7,0,0,0,0,2,0,0,0]
              ,[0,4,0,0,1,0,5,0,0]
              ,[0,0,0,0,0,0,0,0,0]
              ,[6,0,0,1,0,0,0,7,0]
              ,[0,0,0,0,0,6,1,0,9]
              ,[9,2,0,0,0,0,0,0,6] ])

def img2arr(imgDir):
	img = cv2.imread(imgDir, 0)
	img = cropGameBoard(img)
	img = cv2.bitwise_not(img)	
	# return zz, img;

	img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]

	# w, h, p = 44, 47, 4
	w, h, p = int(img.shape[0]/9.7), int(img.shape[1]/9), 4
	imgs = []
	img2 = img.copy()

	for i in range(9):
		for j in range(9):
			start = (j*(w+p), p+h*i)
			end = (start[0]+w, start[1]+h)
			boxW = start[1] - start[0]
			boxH = end[1] - end[0]
			# cv2.rectangle(img2, (start[0], start[1]), end, (0,255,0), 2)
			# cv2.circle(img2, (start[0]+20, start[1]+20), 5, (0,255,0), 2)
			imgs.append(img[start[0]:end[0], start[1]:end[1]])


	digits = []
	print('\nOCR started.\nPlease wait...')
	c = 0
	for n in imgs:
		c = c + 1
		currentCell = pytesseract.image_to_string(n, config='--psm 6') # reads digits
		if (currentCell):
			digits.append(int(currentCell))
		else:
			digits.append(0)


	arr = np.reshape(digits, (9,9))
	arr = np.transpose(arr)
	print('OCR complete.')
	# cv2.imshow(imgDir, img2)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	return arr, img


def cropGameBoard(img):
	img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
	template = cv2.imread('image/gameBoard.png', 0)
	k = 1.45
	template = cv2.resize(template, (int(template.shape[1]*k), int(template.shape[0]*k)))
	h, w = template.shape
	result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	bottom_right = (max_loc[0] + w, max_loc[1] + h)	
	# cv2.rectangle(img, max_loc, bottom_right, 255, 1)
	img3 = img.copy()
	img3 = img3[max_loc[1]-5:bottom_right[1], max_loc[0]:bottom_right[0]]
	# cv2.imshow("3", img3)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	return img3
