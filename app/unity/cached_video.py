# -*- coding: utf-8 -*-
import cv2, os, weakref

from . import cache

class VideoCamera():

    __metaclass__ = cache.Cached

    def __init__(self, index):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        #self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        self.seed = cv2.VideoCapture(os.path.join(app.root_path, 'main/static/video/video{}.mp4'.format(index)))
        self.video = []
        while True:
            success, image = self.seed.read()
            if success:
                self.video.append(image)
            else:
                break
    
    def __del__(self):
	del(self.video)
        self.seed.release()

    def get_frame(self):
        for image in self.video:
            ret, jpeg = cv2.imencode('.jpg', image)
            yield jpeg.tostring()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
