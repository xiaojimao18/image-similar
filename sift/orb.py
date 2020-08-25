import cv2
import numpy as np

# img = cv2.imread('../1.png', 0)
# orb = cv2.ORB_create()

# kp, des = orb.detectAndCompute(img, None)

# img2 = cv2.drawKeypoints(img, kp, img, color=(0,255,0), flags=0)
# cv2.imwrite('orb_keypoints.jpg', img2)

img = cv2.imread("../1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
kp = orb.detect(gray, None)

cv2.drawKeypoints(gray, kp, img)
cv2.imwrite("orb_keypoints.jpg", img)
