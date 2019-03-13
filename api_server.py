#!/usr/bin/env python3
from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from OP_RETURN import *
import re
import json

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

request_parser = RequestParser(bundle_errors=True)


class Blockchain(Resource):
    def get(self, ref):
        regexp_pattern = '^\d{1,8}-\d{6}$'
        sanity_check = re.match(regexp_pattern, ref)
        if sanity_check:
            result = OP_RETURN_retrieve(ref)
            # first we need to process the stored data for consumption
            for idx, val in enumerate(result):
                # convert data from string to data structure
                decoded_data = result[idx]['data'].decode('utf-8')
                result[idx]['data'] = json.loads(decoded_data)
            return(result)
        else:
            return({"error": "Please provide a valid reference."})


class BlockchainStore(Resource):
    def post(self):
        json_data = request.get_json()
        result = OP_RETURN_store(json.dumps(json_data))
        return(result)


api.add_resource(Blockchain, '/blockchain/<ref>')
api.add_resource(BlockchainStore, '/blockchain')

if __name__ == '__main__':
    app.run(debug=True)
