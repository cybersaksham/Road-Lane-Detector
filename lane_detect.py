import cv2
import numpy as np


def drawLane(img, ROI_image):
    lines = cv2.HoughLinesP(ROI_image,
                            rho=2,
                            theta=np.pi / 60,
                            threshold=50,
                            lines=np.array([]),
                            minLineLength=40,
                            maxLineGap=100)
    img = np.copy(img)
    line_image = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 3)
    img = cv2.addWeighted(img, 0.8, line_image, 1, 0.0)
    return img


def LaneDetect(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(gray_image, 50, 120, apertureSize=3)
    return canny_image
