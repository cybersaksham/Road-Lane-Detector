import numpy as np
import ROI
import lane_detect


def process(road):
    # Detecting Lane
    canny_image = lane_detect.LaneDetect(road)

    # Finding region of interest
    height = road.shape[0]
    width = road.shape[1]
    roi_vertices = [
        (0, height),
        (width / 2, height / 2),
        (width, height)
    ]
    masked_image = ROI.ROI(canny_image, np.array([roi_vertices], np.int32))

    # Drawing lines
    lane_image = lane_detect.drawLane(road, masked_image)

    return lane_image
