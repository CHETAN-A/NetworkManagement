from flask import current_app
from collections import deque

import re
# print(('args', args), ('kwargs', kwargs))

device_name_regex = r'^[A-Za-z_]\w+$'


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
        if requestData['type'] not in ('COMPUTER', 'REPEATER'):
            return response("type '{}' is not supported".format(requestData['type']), 400)

        elif requestData['name'] in network.nodes:
            return response("Device '{}' already exists".format(requestData['name']), 400)

        elif not re.search(device_name_regex, requestData['name']):
            return response("Device '{}' name is not valid".format(requestData['name']), 400)

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
        if node not in network.nodes:
            return {
                "msg": "Device '{}' not found".format(node)
            }, 400
        elif not isinstance(requestData['value'], int) or requestData['value'] < 0:
            return {
                "msg": "value should be an +ve integer"
            }, 400

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
        if not isinstance(source, str) or\
            not re.search(device_name_regex, source):
            return response("Invalid source type", 400)
        
        # To check if target nodes type and pattern is valid
        elif not isinstance(targets, list) or\
            any(map(lambda inp: not isinstance(inp, str), targets)) or\
            any(map(lambda inp: not re.search(device_name_regex, inp), targets)):
            return response("Invalid targets type", 400)
        
        # To check if source is present in network nodes list
        elif source not in network.nodes:
            return response("Device '{}' not found".format(source), 400)
        
        # To check if target nodes are present in network nodes list
        elif any(map(lambda inp: inp not in network.nodes, targets)):
            return response("Device(s) in targets is not found", 400)
        
        validTargetNodes = set()
        for node in targets:
            if source == node:
                return response("Cannot connect device to itself", 400)
            elif source not in network.nodes[node]['connections']:
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
            return response('Invalid Request', 400)
                
        matcher = re.search(r'^from=(?P<source>[A-Za-z_]\w+)&to=(?P<target>[A-Za-z_]\w+)$', args[0])
        if not matcher:
            return response('Invalid Request', 400)

        queryParams = matcher.groupdict()
        source, target = queryParams['source'], queryParams['target']

        # Loads the network object to access the current nodes present in the network
        network = current_app.config['network']

        # Validating source and target nodes
        if source not in network.nodes:
            return response("Device '{}' not found".format(source), 400)
        elif target not in network.nodes:
            return response("Device '{}' not found".format(target), 400)
        elif network.nodes[source]['type'] != 'COMPUTER' or network.nodes[target]['type'] != 'COMPUTER':
            return response("Route cannot be calculated with repeater", 400)

        # find shortest path between source and target node
        route = network.findRoute(source, target)

        if route:
            return response("Route is {}".format('->'.join(route)), 200)
        # if no route found return the same msg
        else: 
            return response('Route not found', 400)




def response(message, status):
    return {
        'msg': message
    }, status