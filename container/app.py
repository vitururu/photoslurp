import csv
import requests

from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

class DetectFormat(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('url')
            args = parser.parse_args()
            url = args['url']
            if 'csv' in url.split('.')[-1]:
                return {'url': url, 'format': 'csv'}
            if 'tsv' in url.split('.')[-1]:
                return {'url': url, 'format': 'tsv'}
            if 'xml' in url.split('.')[-1]:
                return {'url': url, 'format': 'xml'}
            catalog = requests.get(url, allow_redirects=True)
            decoded_catalog = catalog.content.decode("utf-8") 
            if decoded_catalog.startswith('<?xml version="1.0" encoding="UTF-8"?>'):
                return {'url': url, 'format': 'xml'}
            dialect = csv.Sniffer().sniff(decoded_catalog)
            if dialect.delimiter == '|':
                return {'url': url, 'format': 'tsv'}
            elif dialect.delimiter == ',':
                return {'url': url, 'format': 'csv'}
            else:
                return {'url': url, "error": "File format unknown or not recognizable."}
        except:
            return {'url': url, "error": "File format unknown or not recognizable."}
api.add_resource(DetectFormat, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
