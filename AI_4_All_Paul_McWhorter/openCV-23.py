import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX
donFace=FR.load_image_file('/home/abdul/Documents/GitHub/AI_Examples/AI_Examples/AI_4_All_Paul_McWhorter/demoImages/known/Donald Trump.jpg')
faceLoc=FR.face_locations(donFace)[0]
print(faceLoc)
top,right,bottom,left=faceLoc
cv2.rectangle(donFace,(left,top),(right,bottom),(255,0,0),3)
donFaceBGR=cv2.cvtColor(donFace,cv2.COLOR_RGB2BGR)
cv2.imshow('My_Window',donFaceBGR)
cv2.waitKey(5000)