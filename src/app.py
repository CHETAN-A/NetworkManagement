from flask import Flask, request, jsonify
from flask_restful import Api
from flask_restful import Resource

from resources.model import NetworkDeviceManager
from resources.urls import methodMatcher
from resources.validations import ValidationError
from resources.utils import ( clean_str, response,
    RequestValidator, exception_handler)

import os

class NetworkManager(Resource):

    def post(self):
        # print(request.get_data(as_text=True))
        requestPacket = request.get_data(as_text=True).split('\n')
        print(requestPacket)
        requestPacketLen = len(requestPacket)

        # Getting the command type and command
        try:
            commandType, command = requestPacket[0].strip().split(' ')
        except (ValueError):
            raise ValidationError('Invalid Command', 400)

        # Get query parameters if exists
        requestCommand, requestQueryParams = command.strip().split('?') if '?' in command else (command, None)

        # Get Command Headers
        headers = {}
        i = 1
        while i < requestPacketLen and requestPacket[i].strip():
            try:
                headerName, headerValue = requestPacket[i].strip().split(':')
            except ValueError:
                raise ValidationError('Invalid Command', 400)
                
            headers[headerName.strip()] = headerValue.strip()
            i += 1

        # Get Command data
        i += 1
        requestBody = ''
        while i < requestPacketLen:
            requestBody += requestPacket[i].strip()
            i += 1

        # Validate the Command
        validator = RequestValidator(
            commandType,
            requestCommand,
            headers,
            requestBody
        )
        validatedInputs = validator.validate()

        return validatedInputs['view'](requestQueryParams, **validatedInputs['inputs'])

app = Flask(__name__)
api = Api(app)
app.config["BASE_DIR"] = os.path.dirname(os.path.abspath(__file__))

api.add_resource(NetworkManager, '/ajiranet/process')

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == '__main__':
    network = NetworkDeviceManager()
    app.config['network'] = network
    app.run(threaded=True, port=8080, debug=True)