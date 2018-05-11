import cv2
import os
import numpy as np
import pickle
from src.lib import detect_face

dictionary_people = dict()
dir_name = "data"

def prepare_training_data():    
    nb_people = 0

    faces, labels = [], []
    
    subject_folder_names = os.listdir(dir_name)

    print('Training for {}'.format(', '.join(subject_folder_names)))
    for folder_name in subject_folder_names:

        dictionary_people[nb_people] = folder_name
        
        folder_path = os.path.join(dir_name, folder_name)
        
        subject_images_names = os.listdir(folder_path)

        for image_name in subject_images_names:

            image_path = os.path.join(folder_path,image_name)

            #read image
            image = cv2.imread(image_path)

            #detect face
            face, _ = detect_face(image)

            if face is not None:
                #add face to list of faces
                faces.append(face)
                #add label for this face
                labels.append(nb_people)
            else:
                print("Impossible to find {}".format(folder_name))
          
        nb_people = nb_people+1
    
    return faces, labels

print("Preparing data...")
faces, labels = prepare_training_data()
print("Data prepared")

#print total faces and labels
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))


face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.train(faces, np.array(labels))

face_recognizer.save('model/model.xml')

with open('model/dict.pickle', 'wb') as handle:
    pickle.dump(dictionary_people, handle, protocol=pickle.HIGHEST_PROTOCOL)
    