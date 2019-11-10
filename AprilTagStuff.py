#!/usr/bin/env python3

import cv2
import apriltag
import numpy as np


def scan_image(i):
    detector = apriltag.Detector()
    dets = detector.detect(i)
    retval = {}

    for d in dets:
        retval[(d.tag_family, d.tag_id)] = (d.center, d.corners)

    return retval


def get_tags(img1):
    tags = scan_image(img1)
    return [t[0] for t in tags.keys()]


def calculate_travel(img1, img2):
    tags1 = scan_image(img1)
    tags2 = scan_image(img2)
    distances = {}
    shared_tags = set(tags1.keys()) & set(tags2.keys())

    for tag in shared_tags:
        d1_center = tags1[tag][0]
        d2_center = tags2[tag][0]
        distances[tag] = np.sqrt((np.power(d2_center[0], 2) - np.power(d1_center[0], 2))
                                 + (np.power(d2_center[1], 2) - np.power(d1_center[1], 2)))
    return distances


def highlight_image(img):
    tags = scan_image(img)
    homography = None
    copy = img.copy()

    for tag in tags:
        matrix = tags[tag][1]
        homography = cv2.polylines(copy, [np.int32(matrix)], True, (255, 0, 0), 3)

    if homography.size > 0:
        return homography
