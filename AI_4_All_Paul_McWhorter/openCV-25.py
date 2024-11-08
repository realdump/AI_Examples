import os
import cv2
import face_recognition as FR
print(cv2.__version__)
imageDir='/home/abdul/Documents/GitHub/AI_Examples/AI_Examples/AI_4_All_Paul_McWhorter/demoImages/known'
for root,dirs,files in os.walk(imageDir):
    print('my present directory(root):', root)
    print('Dirs in root', dirs)
    print('My Files in root', files)
    for file in files:
        print('Your Guy Is:', file)
        fullFilePath=os.path.join(root,file)
        print(fullFilePath)
        print(root+file)