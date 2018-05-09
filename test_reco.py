import cv2
import os
import numpy as np
import pickle
from src.lib import detect_face


face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('model/model.xml')

with open('model/dict.pickle', 'rb') as handle:
    dictionary_people = pickle.load(handle)

def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    

def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    
    face, rect = detect_face(frame)

    #predict the image using our face recognizer 
    if face is not None:
        id_label ,conf = face_recognizer.predict(face)
        
        if conf>65 : 
            #get name of respective label returned by face recognizer
            label_text = dictionary_people[id_label] + " " + str(int(conf))+"%"
        else:
            label_text="Unknown"
    
        #draw a rectangle around face detected
        draw_rectangle(frame, rect)

        #draw name of predicted person
        draw_text(frame, label_text, rect[0], rect[1]-5)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
