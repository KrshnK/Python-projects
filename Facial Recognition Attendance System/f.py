import face_recognition
import cv2
import csv
import numpy as np
from datetime import datetime

video_capture=cv2.VideoCapture(0)
#Load known faces 

harry_image=face_recognition.load_image_file("harry.jpg")
harry_encoding=face_recognition.face_encodings(harry_image)[0]

known_face_encodings=[harry_encoding]
known_face_names=["harry"]

#list of expected students

student = known_face_names.copy()

face_location=[]
face_encodings=[]

# Get the current date and time

now=datetime.now()
current_date=now.strftime("%y-%m-%d")

f=open(f"{current_date}.csv","wt",newline="")
lnwriter=csv.writer(f)

while True:
    _, frame=video_capture.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame=cv2.cvtColor(small_frame,cv2.COLOR_BAYER_BG2RGB)

    #RECOGNIZE faces
    face_locations=face_recognition.face_locations(rgb_small_frame)
    face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)

    for face_encoding in face_encodings:
        matches=face_recognition.compare_faces(known_face_encodings,face_encoding)
        face_distance=face_recognition.face_distance(known_face_encodings,face_encoding)

        best_match_index=np.argmin(face_distance)
        if(matches[best_match_index]):
            name = known_face_names[best_match_index]
        
        #add the text if a person is present 
        if name in known_face_names:
            font=cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10,100)
            fontScale = 1.5
            fontColor = (255,0,0)
            thickness = 3
            lineType = 2
            cv2.putText(frame,name+"Present",bottomLeftCornerOfText,font,fontScale,fontColor,thickness,lineType)
            
            if name in student:
                student.remove(name)
                current_time=now.strftime("%H-%M-%S")
                lnwriter.writerow([name,current_time])

    cv2.imshow("Attendance",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video_capture.release()
cv2.destroyAllWindows()
f.close()
