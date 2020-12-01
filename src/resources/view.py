from flask import current_app
from collections import deque

from .validations import NetworkValidation, ValidationError

import re

validator = NetworkValidation()

class Devices:

    def get(self, *args, **kwargs):
        """
            Gives the list of devices present in the network nodes list
        """
        # Loads the network object to access the current nodes present in the network
        network = current_app.config['network']
        context = {
            'devices': network.getNodes()
        }
        return context, 200

    def post(self, *args, **kwargs):
        """
            Adds a new device into the network.
            expected data: type('COMPUTER', 'REPEATER'), name(r'^[A-Za-z_]\w+$')
        """
        requestData = kwargs['data']

        # Loads the network object to access the current nodes present in the network
        network = current_app.config['network']

        # Data Validations
        requestData['isAbsent'] = requestData['name']
        validator.validate(**requestData)

        # Add the device into the network nodes list
        network.addNode(requestData['name'], requestData['type'])

        return response("Successfully added {}".format(requestData['name']), 200)

    def put(self, *args, **kwargs):
        """
            Modify strength of the existing device present in the network nodes list.
            expected data: value(+ve int)
        """
        node = kwargs['uriParams']['name']
        requestData = kwargs['data']

        # Loads the network object to access the current nodes present in the network
        network = current_app.config['network']
        
        # Data Validations
        requestData['isPresent'] = node
        validator.validate(**requestData)

        # update the strength of the device node
        network.updateStrength(node, requestData['value'])

        context = {
            'msg': 'Successfully defined strength'
        }
        return context, 200

class Connections:
    def post(self, *args, **kwargs):
        """
            Add a connection between existing devices
            expected data: source(node), targets(list(nodes))
        """
        requestData = kwargs['data']

        # Loads the network object to access the current nodes present in the network
        network = current_app.config['network']

        source = requestData['source']
        targets = requestData['targets']

        # Data Validations
        # To check if source type and pattern is valid
        if not isinstance(targets, list):
            raise ValidationError("Invalid targets type", 400)
        validator.validate_name(source)
        validator.validate_is_node_present(source)

        # To check if target nodes type and pattern is valid
        for target in targets:
            validator.validate_name(target)
            validator.validate_is_node_present(target)
        
        validTargetNodes = set()
        for node in targets:
            if source == node:
                return response("Cannot connect device to itself", 400)
            elif not network.areNodesConnected(source, node):
                validTargetNodes.add(node)
            else:
                return response("Devices {} and {} are already connected".format(source, node), 400)

        for node in validTargetNodes:
            network.addConnection(source, node)

        return response('Successfully Connected', 200)

class Routes:
    def get(self, *args, **kwargs):
        """
            Get a route between two exiting computer nodes present in the network nodes list
        """
        # Validating Request Query Parameters
        if not isinstance(args, tuple) or not isinstance(args[0], str):
            raise ValidationError('Invalid Request', 400)
                
        matcher = re.search(r'^from=(?P<source>[A-Za-z_]\w+)&to=(?P<target>[A-Za-z_]\w+)$', args[0])
        if not matcher:
            raise ValidationError('Invalid Request', 400)

        queryParams = matcher.groupdict()
        source, target = queryParams['source'], queryParams['target']

        # Loads the network object to access the current nodes present in the network
        network = current_app.config['network']

        # Validating source and target nodes
        for node in (source, target):
            validator.validate_is_node_present(node)

        if not network.isNodeOfType(source, 'COMPUTER') or not network.isNodeOfType(target, 'COMPUTER'):
            raise ValidationError("Route cannot be calculated with repeater", 400)

        # find route between source and target node
        route = network.findRoute(source, target)

        return response("Route is {}".format('->'.join(route)), 200) if route else response('Route not found', 400)


def response(message, status):
    return {
        'msg': message
    }, status