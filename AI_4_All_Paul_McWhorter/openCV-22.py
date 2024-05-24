import cv2
print(cv2.__version__)
import time
width=640
height=360
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceCasCade=cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
eyeCasCade=cv2.CascadeClassifier('haar/haarcascade_eye.xml')
fps=10
timeStamp=time.time()
while True:
    ignore,  frame = cam.read()
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCasCade.detectMultiScale(frameGray,1.3,5)

    for face in faces:
        x,y,w,h=face
        #print('x=',x,'y=',y,'width=',w,'height=',h)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        #frameROI=frame[y:y+h,x:x+w]
        #frameROIGray=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
        #eyes=eyeCasCade.detectMultiScale(frameROIGray)
        
    #print(faces)
    #
    eyes=eyeCasCade.detectMultiScale(frameGray,1.3,5)
    for eye in eyes:
        x,y,w,h=eye
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    loopTime=time.time()-timeStamp
    timeStamp=time.time()

    fpsNew=1/loopTime
    fps=.9*fps+.1*fpsNew
    fps=int(fps)
    #print(fps)
    cv2.putText(frame,str(fps)+' fps',(5,30),cv2.FONT_HERSHEY_PLAIN,2,(0,255,255),2)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()