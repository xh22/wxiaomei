# -*- coding: utf-8 -*-
import os

from flask import session, render_template, request, redirect, Response
from flask.views import MethodView

from main import app, db

import cv2

class VideoCamera(object):
    def __init__(self, index):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        #self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        self.video = cv2.VideoCapture('main/static/video/video{}.mp4'.format(index))
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tostring()

@app.route('/news')
def news():
    return render_template('news.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed/<int:index>')
def video_feed(index):
    return Response(gen(VideoCamera(index)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

