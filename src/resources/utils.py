from flask import current_app
from .urls import methodMatcher
from .validations import ValidationError

import re
import functools
import logging
import json


clean_str = lambda string: string.encode('utf-8').strip() if not isinstance(string, bytes) else string.decode('utf-8').strip()

class RequestValidator:
    def __init__(self, *args):
        super().__init__()
        ( self.commandType, self.requestCommand,
         self.requestHeaders, self.requestBody ) = args
        self.methodObj = {}
        self.matchedURIObj = None
        self.uriParams = None

    def validate_command_type(self):
        if self.commandType not in methodMatcher:
            raise ValidationError('Invalid Command', 400)

    def validate_uri(self):

        for uriObj in self.methodObj['uris']:
            matcher = re.search(uriObj['uri'], self.requestCommand)
            if matcher:
                self.uriParams = matcher.groupdict()
                self.matchedURIObj = uriObj
                return
        raise ValidationError('Invalid Command', 400)

    def validate_headers(self):
        for header in self.matchedURIObj['headers'].keys():
            if header not in self.requestHeaders or \
                self.requestHeaders[header] != self.matchedURIObj['headers'][header]:
                raise ValidationError('Invalid Command', 400)

    def validate_body(self):
        requestData = None
        
        if self.matchedURIObj['data'] and 'content-type' in self.requestHeaders and \
            self.requestHeaders['content-type'] == 'application/json':
            try:
                requestData = json.loads(self.requestBody)
                for data in self.matchedURIObj['data']:
                    if data not in requestData:
                        raise ValidationError('Invalid Command', 400)
            except Exception as err:
                raise ValidationError('Invalid Command', 400)

        return requestData

    def validate(self):
        # Match the command Type
        self.validate_command_type
        self.methodObj = methodMatcher[self.commandType]

        # finding the match with the respective URI
        self.validate_uri()

        # validating the headers
        self.validate_headers()
        
        # Validating the command body
        requestData = self.validate_body()

        inputs = {
            "inputs" : {
                'data': requestData,
                'uriParams': self.uriParams
            },
            'view': self.matchedURIObj['view']
        }

        return inputs

def response(message, status):
    return {
        'msg': message
    }, status

def exception_handler(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print(err)
            raise ValidationError('Internal Server Error', 500)
    return wrapper