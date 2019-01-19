#!/usr/bin/python
import os
from flask_restful import Resource
from flask_restful import reqparse
from flask import render_template, request
from flask import send_from_directory
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

class ModelRepoService(Resource):


    def __init__(self):
        self.model_file_dir = '/home/aknatva/mdef/models/'
        self.allowed_extensions = set(['txt', 'pb', 'pmml', 'h5', 'gz'])
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('modelName', type = str, required = True, help = 'Need Model Name', location = 'args')
        self.parser.add_argument('appName', type = str, required = True, help = 'Need App Name', location = 'args')
        self.parser.add_argument('modelVersion', type = str, required = True, help = 'Need Model Version', location = 'args')
        self.parser.add_argument('modelFile',type = FileStorage, location = 'files')

        super(ModelRepoService, self).__init__()


    def get(self):
        args = self.parser.parse_args()
        print(type(args))
        appname = args['appName']
        modelname = args['modelName']
        modelversion = args['modelVersion']
        path = appname + "/" + modelname + "/" + modelversion
        full_path = os.path.join(self.model_file_dir,path)
        print("path is : ", full_path)
        if not os.path.isdir(full_path):
            return {"message" : "Model File not Found"}, 404
        if os.path.isfile(full_path):
            return {"message" : "The Path should be a directory, verify your arguments"}, 404
        if len(os.listdir(full_path)) == 1:
            for fname in os.listdir(full_path):
                return send_from_directory(full_path,fname,as_attachment=True)
                return {"message" : "Successfully downloaded Model File" }



    def post(self):
        if request.method == 'POST':
            if 'modelFile' in self.parser.parse_args():
                flash('No file part')
                return {'message' : 'Model File path should be associated with argument modelFile' }
            args = self.parser.parse_args()
            appName = args['appName']
            modelName = args['modelName']
            modelVersion = args['modelVersion']
            modelFile = args['modelFile']
            if args['modelFile'] == '':
                flash('No selected file')
                return redirect(self.parser.url)
#           if modelFile and allowed_file(modelFile.filename):
            filename = secure_filename(modelFile.filename)
            modelFile.save(os.path.join(self.model_file_dir, appName, modelName, modelVersion, filename))
            return {'message' : 'Successfully uploaded the Model file' }
        return ''


#    def allowed_file(filename):
#        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

