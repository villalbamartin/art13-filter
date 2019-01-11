#!/usr/bin/python3

from filter import Filter
from flask import Flask, request, abort
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Upload(Resource):

    def post(self, file):
        f = Filter()
        file = request.form.get('file')
        retval = f.query(file)
        return retval[''], 403
