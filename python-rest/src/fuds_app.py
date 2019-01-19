# curl 'http://xxx.xx.xxx.xx:5080/mdef/api/v1/modelrepos?folder=abcd&folder2=efgh'

import os, sys
from flask import Flask, jsonify, abort, request, send_from_directory
from flask import make_response,render_template
from flask import current_app

from flask_restful import Resource, Api
from flask_restful import reqparse

from flask_marshmallow import Marshmallow

from model_repo_service import ModelRepoService
from model_exec_stats_service import ModelExecStatsService

MODEL_REPO_DIRECTORY = '/home/aknatva/mdef/models'

app = Flask(__name__,template_folder='templates')


@app.route('/')
def index():
    return render_template('home.html')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


api = Api(app,prefix="/mdef/api/v1")

api.add_resource(ModelRepoService, '/modelrepos', endpoint='modelrepos')
api.add_resource(ModelExecStatsService, '/modelexecstats', endpoint='modelexecstats')


if __name__ == '__main__':
    app.run('0.0.0.0',port=5080,debug=True)
