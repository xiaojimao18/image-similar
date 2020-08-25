import cv2
import numpy as np

img = cv2.imread("../1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)

cv2.drawKeypoints(gray, kp, img)
cv2.imwrite("sift_keypoints.jpg", img)
