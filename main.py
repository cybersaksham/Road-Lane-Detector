import matplotlib.pylab as plt
import cv2
import process

road = cv2.imread("road.png")

lane_image = cv2.cvtColor(process.process(road), cv2.COLOR_BGR2RGB)
plt.imshow(lane_image)
plt.show()

# road = cv2.VideoCapture("road.mp4")
#
# while road.isOpened():
#     _, frame = road.read()
#     frame = process.process(frame)
#     cv2.imshow("Road", frame)
#     if cv2.waitKey(1) == 27:
#         break
#
# road.release()
# cv2.destroyAllWindows()
