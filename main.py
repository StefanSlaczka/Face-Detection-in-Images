import cv2
import tensorflow as tf

image = cv2.imread('./data/test-image/test.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Blue rectangle


cv2.imshow('Image with Face Detected', image)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()