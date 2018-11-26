# -*- coding: utf-8 -*-

import os
import json
import requests
import tempfile

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

from label_image import get_result


UPLOAD_FOLDER = './images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app, support_credentials=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/detector", methods=['POST'])
@cross_origin()
def receive_message():
    if request.method == 'POST':
        print(request.files)
        print(request.data)
        print(request.headers['Content-Type'])

        if request.headers['Content-Type'] == 'image/jpeg':
            tf = tempfile.NamedTemporaryFile(buffering=-1, dir='images')
            print(tf.name)

            filename = '{}.{}'.format(tf.name, request.headers['Content-Type'].split('/')[1])

            with open(filename, 'wb') as f:
                f.write(request.data)
        else:
            if 'file' in request.files:
                file = request.files['file']
                print(file)
            elif 'image' in request.files:
                file = request.files['image']
            else:
                return jsonify('No file present')

            if file.filename == '':
                return jsonify('No selected file')

            if file and allowed_file(file.filename.lower()):
                filename = secure_filename(file.filename.lower())
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        result = get_result(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify(result)


if __name__ == "__main__":
    app.run(threaded=True)