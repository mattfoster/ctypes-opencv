#!/usr/bin/env python
# Webcam demo

from opencv import *

win = 'Show Cam'

if __name__ == '__main__':  
  cvNamedWindow(win)
  cap = cvCreateCameraCapture(0)
  while cvWaitKey(1) != 27:
      img = cvQueryFrame(cap)
      gray = cvCreateImage(cvSize(img[0].width, img[0].height), 8, 1)
      edges = cvCreateImage(cvSize(img[0].width, img[0].height), 8, 1)
      cvCvtColor(img, gray, 6)
      cvCanny(gray, edges, 0, 90, 3)
      cvShowImage(win, edges)
      
  cvDestroyWindow(win)
  cvReleaseImage(gray)
  cvReleaseImage(edges)