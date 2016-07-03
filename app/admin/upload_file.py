# -*- coding: utf-8 -*-
import os

from flask.views import MethodView
from flask import session, render_template, request, redirect, flash

from flaskext.uploads import (UploadSet, configure_uploads, IMAGES, AUDIO,
                              UploadNotAllowed)

from main import app

photoscert = UploadSet('photoscert', IMAGES)
configure_uploads(app, photoscert)

photosport = UploadSet('photosport', IMAGES)
configure_uploads(app, photosport)

videos = UploadSet('videos', AUDIO)
configure_uploads(app, videos)

videopic = UploadSet('videopic', IMAGES)
configure_uploads(app, videopic)

class Uplaod_file(MethodView):
    def save(self, host, name, root):
        try:
            filename = host.save(request.files[name])
        except UploadNotAllowed:
            flash(u"上传失败!")
        else:
            if filename != request.files[name].filename:
                os.system("mv '{0}''{1}' '{0}''{2}'".format(
                    app.config[root], filename, request.files[name].filename))
            flash(u"上传成功!")

    def post(self):
        print request.files
        if 'photocert' in request.files:
            self.save(photoscert, 'photocert', 'UPLOADED_PHOTOSCERT_DEST')
        elif 'photoport' in request.files:
            self.save(photosport, 'photoport', 'UPLOADED_PHOTOSPORT_DEST')
        elif 'video' in request.files:
            self.save(videos, 'video', 'UPLOADED_VIDEOS_DEST')
        elif 'video-pic' in request.files:
            self.save(videopic, 'videopic', 'UPLOADED_VIDEOPIC_DEST')
        return redirect('/admin/upload_file')

app.add_url_rule('/admin/upload_file', view_func=Uplaod_file.as_view('upload_file'))
