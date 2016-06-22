# -*- coding: utf-8 -*-
import os

from flask import session, render_template, request, redirect, Response
from flask.views import MethodView

from main import app, db
from unity import cached_video, file_video

@app.route('/news')
def news():
    return render_template('news.html')

def gen(camera):
    for frame in camera.get_frame():
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen_file(camera):
    while True:
	frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

class Video_feed(MethodView): 
    def get(self, index):
    	#return Response(gen(cached_video.VideoCamera(index)),
        return Response(gen_file(file_video.VideoCamera(index)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

app.add_url_rule('/video_feed/<int:index>', view_func=Video_feed.as_view('video_feed'))
