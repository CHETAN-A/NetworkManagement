# from .utils import ValidationError as ValidationHandler
from flask import current_app
import re

device_name_regex = r'^[A-Za-z_]\w+$'

class NetworkValidation:
    def __init__(self):
        super().__init__()
        self.validate_data = {
            'name': self.validate_name,
            'type': self.validate_type,
            'value': self.validate_value,
            'isPresent': self.validate_is_node_present,
            'isAbsent': self.validate_is_node_absent,
        }
    
    def validate(self, *args, **kwargs):
        # print(kwargs)
        for key in kwargs.keys():
            if key in self.validate_data:
                self.validate_data[key](kwargs[key])

    def validate_name(self, name):
        if not isinstance(name, str) or\
            not re.search(device_name_regex, name):
            raise ValidationError("Device '{}' name is not valid".format(name), 400)
    
    def validate_type(self, nodeType):
        if nodeType not in ('COMPUTER', 'REPEATER'):
            raise ValidationError("type '{}' is not supported".format(nodeType), 400)
    
    def validate_value(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValidationError("value should be an +ve integer", 400)

    def validate_is_node_present(self, name):
        network = current_app.config['network']
        if not network.isNodePresent(name):
            raise ValidationError("Device '{}' not found".format(name), 400)
    
    def validate_is_node_absent(self, name):
        network = current_app.config['network']
        if network.isNodePresent(name):
            raise ValidationError("Device '{}' already exists".format(name), 400)

class ValidationError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        resp = dict(self.payload or ())
        resp['msg'] = self.message
        return resp