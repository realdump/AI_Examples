import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX
width=1280
height=720
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) 
#cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter.fourcc('M','P','4','V'))

abdFace=FR.load_image_file('/home/abdul/Documents/GitHub/AI_Examples/AI_Examples/AI_4_All_Paul_McWhorter/demoImages/known/Abdul.png')
faceLoc=FR.face_locations(abdFace)[0]
abdFaceEncode=FR.face_encodings(abdFace)[0]


nancyFace=FR.load_image_file('/home/abdul/Documents/GitHub/AI_Examples/AI_Examples/AI_4_All_Paul_McWhorter/demoImages/known/Nancy Pelosi.jpg')
faceLoc=FR.face_locations(nancyFace)[0]
nancyFaceEncode=FR.face_encodings(nancyFace)[0]

penceFace=FR.load_image_file('/home/abdul/Documents/GitHub/AI_Examples/AI_Examples/AI_4_All_Paul_McWhorter/demoImages/known/Mike Pence.jpg')
faceLoc=FR.face_locations(penceFace)[0]
penceFaceEncode=FR.face_encodings(penceFace)[0]

knownEncodings=[abdFaceEncode,nancyFaceEncode,penceFaceEncode]
names=['Abdul Majeed','Nancy Pelosi','Mike Pence']

while True:
    ignore,  unknownFace= cam.read()
    unknownFaceRGB=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
    faceLocations=FR.face_locations(unknownFaceRGB)
    unknownEncodings=FR.face_encodings(unknownFaceRGB,faceLocations)

    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left=faceLocation
        print(faceLocation)
        cv2.rectangle(unknownFace,(left,top),(right,bottom),(255,0,0),3)
        name='Unknown Person'
        matches=FR.compare_faces(knownEncodings,unknownEncoding)
        print(matches)
        if True in matches:
            matchIndex=matches.index(True)
            print(matchIndex)
            print(names[matchIndex])
            name=names[matchIndex]
        cv2.putText(unknownFace,name,(left,top),font,.75,(0,0,255),2)

    cv2.imshow('My Faces',unknownFace)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
