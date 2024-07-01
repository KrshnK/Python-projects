import face_recognition
import cv2
import csv
import numpy as np
from datetime import datetime

# Initialize the video capture device
video_capture = cv2.VideoCapture(0)

# Load the known face image and encoding
krishna_image = face_recognition.load_image_file("C:\\Users\\91886\\Desktop\\Python-projects\\Facial Recognition Attendance System\\krishna.jpg")
krishna_encoding = face_recognition.face_encodings(krishna_image)[0]

# Create a list of known face encodings and corresponding names
known_face_encodings = [krishna_encoding]
known_face_names = ["krishna"]

# Make a copy of the list of known face names for tracking expected students
student = known_face_names.copy()

# Create empty lists to store face locations and encodings
face_location = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%y-%m-%d")

# Create a CSV file for logging attendance
f = open(f"{current_date}.csv", "wt", newline="")
lnwriter = csv.writer(f)

# Loop through video frames and recognize faces
while True:
    # Read a video frame and resize it to improve processing speed
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    gray_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    rgb_small_frame = cv2.cvtColor(gray_small_frame, cv2.COLOR_GRAY2RGB)

    # Find the locations and encodings of faces in the current frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # Loop through detected face encodings and compare them to known encodings
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)

        # Determine the best match for the detected face
        best_match_index = np.argmin(face_distance)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Add text to the frame if a known person is present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottom_left_corner_of_text = (10, 100)
            font_scale = 1.5
            font_color = (255, 0, 0)
            thickness = 3
            line_type = 2
            cv2.putText(frame, name + " Present", bottom_left_corner_of_text, font, font_scale, font_color, thickness, line_type)

            # If the detected person is expected, remove them from the list of expected students and log their attendance
            if name in student:
                student.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])

    # Display the frame with any added text
    cv2.imshow("Attendance", frame)

    # Exit the loop if the "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture device and close the CSV file
video_capture.release()
cv2.destroyAllWindows()
f.close()
