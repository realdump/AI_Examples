import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX
donFace=FR.load_image_file('/home/abdul/Documents/GitHub/AI_Examples/AI_Examples/AI_4_All_Paul_McWhorter/demoImages/known/Donald Trump.jpg')
faceLoc=FR.face_locations(donFace)[0]
donFaceEncode=FR.face_encodings(donFace)[0]

nancyFace=FR.load_image_file('/home/abdul/Documents/GitHub/AI_Examples/AI_Examples/AI_4_All_Paul_McWhorter/demoImages/known/Nancy Pelosi.jpg')
faceLoc=FR.face_locations(nancyFace)[0]
nanncyFaceEncode=FR.face_encodings(nancyFace)[0]

knownEncoding=[donFaceEncode,nanncyFaceEncode]
names=['Donald Trump','Nancy Pelosi']

unknownFace=FR.load_image_file('/home/abdul/Documents/GitHub/AI_Examples/AI_Examples/AI_4_All_Paul_McWhorter/demoImages/unknown/u5.jpg')
unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
faceLocations=FR.face_locations(unknownFace)
unknownEncodings=FR.face_encodings(unknownFace,faceLocations)

for faceLocation,unknownEncodings in zip(faceLocations,unknownEncodings):
    top,right,bottom,left=faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
    name='Unknown Person'
    matches=FR.compare_faces(knownEncoding,unknownEncodings)
    print(matches)
    if True in matches:
        matchIndex=matches.index(True)
        print(matchIndex)
        print(names[matchIndex])
        name=names[matchIndex]
    cv2.putText(unknownFaceBGR,name,(left,top),font,0.75,(255,0,0),3)


# print(faceLoc)
# top,right,bottom,left=faceLoc
# cv2.rectangle(donFace,(left,top),(right,bottom),(255,0,0),3)
# donFaceBGR=cv2.cvtColor(donFace,cv2.COLOR_RGB2BGR)
cv2.imshow('My_Window',unknownFaceBGR)
cv2.waitKey(10000)