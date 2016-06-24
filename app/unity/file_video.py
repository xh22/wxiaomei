# -*- coding: utf-8 -*-
import cv2, os

from main import app

class VideoCamera(object):
    def __init__(self, index):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        #self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        self.video = cv2.VideoCapture(os.path.join(app.root_path, 'main/static/video/video{}.mp4'.format(index)))
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
	success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 90])
        return jpeg.tostring()

