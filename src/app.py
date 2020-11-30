from flask import Flask, request
from flask_restful import Api
from flask_restful import Resource

from resources.model import NetworkDeviceManager
from resources.urls import methodMatcher
from resources.utils import ( clean_str, exception_handler, requestValidator, response)

import os

class AjiraNet(Resource):

    @exception_handler
    def post(self):
        # print(request.get_data(as_text=True))
        requestPacket = request.get_data(as_text=True).split('\n')
        requestPacketLen = len(requestPacket)

        # Getting the command type and command
        try:
            commandType, command = requestPacket[0].strip().split(' ')
        except (ValueError):
            return response('Invalid Command', 400)  

        # Get query parameters if exists
        if '?' in command:
            requestCommand, requestQueryParams = command.strip().split('?')
        else:
            requestCommand = command
            requestQueryParams = None

        # Get Command Headers
        headers = {}
        i = 1
        while i < requestPacketLen and requestPacket[i].strip():
            try:
                headerName, headerValue = requestPacket[i].strip().split(':')
            except ValueError:
                return response('Invalid Command', 400)
                
            headers[headerName.strip()] = headerValue.strip()
            i += 1

        # Get Command data
        i += 1
        requestBody = ''
        while i < requestPacketLen:
            requestBody += requestPacket[i].strip()
            i += 1

        # Validate the Command
        validation_check, validatedInputs = requestValidator(commandType, requestCommand, headers, requestBody)
        if validation_check == 400:
            return response('Invalid Command', 400)
        else:
            return validatedInputs['view'](requestQueryParams, **validatedInputs['inputs'])


app = Flask(__name__)
api = Api(app)
app.config["BASE_DIR"] = os.path.dirname(os.path.abspath(__file__))

api.add_resource(AjiraNet, '/ajiranet/process')

if __name__ == '__main__':
    network = NetworkDeviceManager()
    app.config['network'] = network
    app.run(threaded=True, port=8080)