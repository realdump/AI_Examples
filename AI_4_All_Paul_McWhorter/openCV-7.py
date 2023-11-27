import cv2
print(cv2.__version__)
height=640
width=380
myRadius=320
myThick=2
myText='Bismillah'
cam=cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    frame[140:250,220:360]=(0,0,255)
    cv2.rectangle(frame,(250,140),(360,220),(0,255,0),2)
    cv2.circle(frame,(360,180),25,(0,0,0),2)
    cv2.putText(frame,myText,(120,60),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0,),2)
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('my WEBcam',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()