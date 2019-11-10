#!/usr/bin/env python3

import cv2
import apriltag
import numpy as np


# (i: Image) -> Dictionary of tuple(tag_family, tag_id): tuple(center: List, corners: List)
# Uses apriltag module to check for apriltags then returns it as a dict
def scan_image(i):
    detector = apriltag.Detector()
    dets = detector.detect(i)
    retval = {}

    for d in dets:
        retval[(d.tag_family, d.tag_id)] = (d.center, d.corners)

    return retval


# (img1: Image) -> List of Tuples
# Returns the tuple of tag_family and tag_id
def get_tags(img1):
    tags = scan_image(img1)
    return tags.keys()


# (img1: Image, img2: Image) -> Dict(Tuple(tag_family, tag_id), Tuple(List, List))
# Calculates travelled distance and returns it as a dict connecting the tuple of tag_family
# and tag_id to the calculated distance
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


# (img: Image) -> (homography: Image)
# Makes a black and white copy of the original image and returns the copy with the apriltags highlighted
def highlight_image(img):
    tags = scan_image(img)
    homography = None
    copy = img.copy()

    for tag in tags:
        matrix = tags[tag][1]
        homography = cv2.polylines(copy, [np.int32(matrix)], True, (255, 0, 0), 2)

    if (homography is not None) and homography.size > 0:
        return homography
