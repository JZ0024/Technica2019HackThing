#!/usr/bin/env python3

import cv2
import apriltag
import numpy as np


def scan_image(i):
    detector = apriltag.Detector()
    dets = detector.detect(i)

    return dets


if __name__ == "__main__":
    img = 'test2.png'
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    dts = scan_image(image)
    homography = None

    for d in dts:
        retval = image.copy()
        matrix = d.corners
        homography = cv2.polylines(image, [np.int32(matrix)], True, (255, 0, 0), 3)

    if homography.size > 0:
        cv2.imshow("Homography", homography)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
