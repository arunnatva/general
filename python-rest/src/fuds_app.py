#example usage
# curl -F 'modelFile=@/home/arun/poc/image_data.csv' http://fileserver.com:5080/fuds/uploads

import os, sys

from flask import Flask, jsonify, abort, request, send_from_directory
from flask import make_response,render_template
from flask import current_app
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask_marshmallow import Marshmallow

from file_operations_service import FileOperationsService

MODEL_REPO_DIRECTORY = '/home/aknatva/fuds/repos'


app = Flask(__name__,template_folder='templates')


@app.route('/')
def index():
    return render_template('home.html')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


api = Api(app,prefix="/fuds")

api.add_resource(FileOperationsService, '/uploads', endpoint='uploads')


if __name__ == '__main__':
    app.run('0.0.0.0',port=5080,debug=True)
