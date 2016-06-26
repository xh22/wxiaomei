# -*- coding: utf-8 -*-
import os

from flask.views import MethodView
from flask import session, render_template, request, redirect, flash

from flaskext.uploads import (UploadSet, configure_uploads, IMAGES, AUDIO,
                              UploadNotAllowed)

from main import app

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

videos = UploadSet('videos', AUDIO)
configure_uploads(app, videos)

class Uplaod_file(MethodView):
    def post(self):
        if 'photo' in request.files:
            try:
                filename = photos.save(request.files['photo'])
            except UploadNotAllowed:
                flash(u"上传失败!")
            else:
                if filename != request.files['photo'].filename:
                    os.system("mv '{0}''{1}' '{0}''{2}'".format(
                        app.config["UPLOADED_PHOTOS_DEST"], filename, request.files['photo'].filename))
                flash(u"上传成功!")
        elif 'video' in request.files:
            try:
                filename = videos.save(request.files['video'])
            except UploadNotAllowed:
                flash(u"上传失败!")
            else:
                if filename != request.files['video'].filename:
                    os.system("mv '{0}''{1}' '{0}''{2}'".format(
                        app.config["UPLOADED_VIDEOS_DEST"], filename, request.files['video'].filename))
                flash(u"上传成功!")
        return redirect('/admin/upload_file')

app.add_url_rule('/admin/upload_file', view_func=Uplaod_file.as_view('upload_file'))
