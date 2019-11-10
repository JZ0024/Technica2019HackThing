#!/usr/bin/env python3

import cv2
from AprilTagStuff import *
import numpy as np
from imutils.video import VideoStream
import imutils
import time
from collections import deque

vs = VideoStream(src=0).start()
time.sleep(2.0)

while True:
    frame = vs.read()

    if frame is None:
        break

    frame = imutils.resize(frame, width=600)
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video Feed", highlight_image(grey_frame))
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

vs.stop()
cv2.destroyAllWindows()
