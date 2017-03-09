from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources=r'/*') # to allow external resources to fetch data
api = Api(app)

parameters = {"height": { 'value': 1024},
              "width": { 'value': 768}}

@api.resource("/")
class url_index( Resource ):
    def get( self ):
       returnMessage = {"message": "Yes, it works" }
       return returnMessage

@api.resource("/streaming/parameters")
class url_parameters( Resource ):
    def get( self ):
        returnMessage = parameters
        return returnMessage

@api.resource("/streaming/parameters/<parameters_name>")
class url_parameters_name( Resource ):
    def get( self, parameters_name ):
        try:
            return parameters[ parameters_name ]
        except KeyError, ex:
            return { "message": "key error '%s' is not a GPIO name"%(gpio_name,) }, 400

#     def put( self, gpio_name ):
#         try:
#             gpios[ gpio_name ]['value'] = request.json['value']
#             return "", 204
#         except KeyError, ex:
#             return { "message": "key error: Either '%s' is not a GPIO name or data is undefined (received: '%s')"%(gpio_name, str(request.form)) }, 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
