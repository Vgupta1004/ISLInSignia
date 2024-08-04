# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 11:35:19 2020

@author: shara
"""

import numpy as np
import cv2
cap = cv2.VideoCapture('hello/img0001-0026.mp4')
while(cap.isOpened()):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame',gray)
  if cv2.waitKey(25) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()