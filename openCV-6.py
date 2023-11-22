import cv2
print(cv2.__version__)
import numpy as np
boardSize=int(input('What Size is your Board?'))
numSquare=int(input('How many squares?'))
squareSize=int(boardSize/numSquare)

darkColor=(0,0,0)
lightColor=(0,0,255)
nowColor=darkColor
while True:
    x=np.zeros([boardSize,boardSize,3],dtype=np.uint8)
    for row in range(0,numSquare):
        for column in range(0,numSquare):
            x[squareSize*row:squareSize*(row+1),squareSize*column:squareSize*(column+1)]=nowColor
            if nowColor==darkColor:
                nowColor=lightColor
            else:
                nowColor=darkColor
        if nowColor==darkColor:
            nowColor=lightColor
        else:
            nowColor=darkColor

    cv2.imshow('My Checkerboard',x)
    if cv2.waitKey(1) == ord('q'):
        break