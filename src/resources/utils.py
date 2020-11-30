from flask import current_app
from .urls import methodMatcher

import re
import functools
import logging
import json


clean_str = lambda string: string.encode('utf-8').strip() if not isinstance(string, bytes) else string.decode('utf-8').strip()

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
            return {
                'error': '%s' %err,
                'msg': 'Internal Server Error'
            }, 500
    return wrapper

def requestValidator(commandType, requestCommand, requestHeaders, requestBody):
    # Match the command Type
    if commandType in methodMatcher:
        methodObj = methodMatcher[commandType]
        matchedURIObj = None
        uriParams = {}
        # finding the match with the respective URI
        for uriObj in methodObj['uris']:
            matcher = re.search(uriObj['uri'], requestCommand)
            if matcher:
                uriParams = matcher.groupdict()
                matchedURIObj = uriObj
                break
            else:
                continue
        if matchedURIObj:
            # validating the headers
            for header in matchedURIObj['headers'].keys():
                if header not in requestHeaders or requestHeaders[header] != matchedURIObj['headers'][header]:
                    # print('Header Error')
                    return 400, None
            
            # Validating the command body
            requestData = None
            if matchedURIObj['data'] and 'content-type' in requestHeaders and requestHeaders['content-type'] == 'application/json':
                try:
                    requestData = json.loads(requestBody)
                    for data in matchedURIObj['data']:
                        if data not in requestData:
                            # print('Data Not Found Error')
                            return 400, None
                except Exception as err:
                    # print('Invalid JSON Data Error')
                    # print('Json Load error', err)
                    return 400, None
            return 200, {
                "inputs" : {
                    'data': requestData,
                    'uriParams': uriParams
                },
                'view': matchedURIObj['view']
            }
        else:
            # print('Invalid Request URI Error')
            return 400, None        
    # print('Invalid Request Method Error')
    return 400, None