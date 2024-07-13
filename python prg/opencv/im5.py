import cv2
import numpy as np

# yellow
lower = np.array([22, 93, 0])
upper = np.array([45, 255, 255])

cam = cv2.VideoCapture(0)
while True:
    ret, img = cam.read()
    img = cv2.bilateralFilter(img, 15, 50, 50)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow(None, img)
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 500:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 225, 0), 2)

    cv2.imshow('mask', mask)
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()
