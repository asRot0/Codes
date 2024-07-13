import cv2
import time

alg = "../haarcascade_frontalface_default.xml"
haar = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(0)

time.sleep(1)
while True:
    _, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(gray, 1.3, 6)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 225, 0), 2)
    # gaussian=cv2.GaussianBlur(img,(21,21),0)
    bil = cv2.bilateralFilter(img, 15, 60, 60)
    flip = cv2.flip(bil, 1)
    cv2.imshow('face', flip)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()
