# -*- coding: utf-8 -*-
import os

from flask.views import MethodView
from flask import session, render_template, request, redirect, flash

from flaskext.uploads import (UploadSet, configure_uploads, IMAGES, ARCHIVES,
                              UploadNotAllowed)

from main import app

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

videos = UploadSet('videos', ARCHIVES)
configure_uploads(app, videos)

class Uplaod_file(MethodView):
    def post(self):
        if 'photo' in request.files:
            try:
                filename = photos.save(request.files['photo'])
            except UploadNotAllowed:
                flash(u"上传失败!")
            else:
                flash(u"上传成功!")
        elif 'video' in request.files:
            try:
                filename = videos.save(request.files['video'])
                os.system("unzip -o '{0}''{1}' -d '{0}'".format(
                    app.config["UPLOADED_VIDEOS_DEST"], filename))
                os.system("rm '{0}''{1}'".format(
                    app.config["UPLOADED_VIDEOS_DEST"], filename))
            except UploadNotAllowed:
                flash(u"上传失败!")
            else:
                flash(u"上传成功!")
        return redirect('/admin/upload_file')

app.add_url_rule('/admin/upload_file', view_func=Uplaod_file.as_view('upload_file'))
