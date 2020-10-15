import auto_face_recognition

obj = auto_face_recognition.AutoFaceRecognition()

obj.datasetcreate(haarcascade_path='haarcascade/haarcascade_frontalface_default.xml',
                  eyecascade_path='haarcascade/haarcascade_eye.xml',
                  class_name='Jay')
obj.face_recognition_train()
obj.predict_faces(class_name=['Dipesh', 'Jay'], color_mode=True)
