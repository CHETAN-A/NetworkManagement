from .view import Connections, Devices, Routes

device = Devices()
connection = Connections()
route = Routes()

createUrls = [
    {
        'uri' : r'^/devices$',
        'view': device.post,
        'headers': {
            'content-type': 'application/json'
        },
        'data': ['type', 'name']
    },
    {
        'uri' : r'^/connections$',
        'view': connection.post,
        'headers': {
            'content-type': 'application/json'
        },
        'data': ['source', 'targets']
    }
]

modifyUrls = [
    {
        'uri' : r'^/devices/(?P<name>[A-Za-z_]\w+)/strength$',
        'view': device.put,
        'headers': {
            'content-type': 'application/json'
        },
        'data': ['value']
    }
]
fetchUrls = [
    {
        'uri' : r'^/info-routes$',
        'view': route.get,
        'headers': {},
        # 'queryParams': r'^from=A\d+&to=A\d+$',
        'data': []
    },
    {
        'uri' : r'^/devices$',
        'view': device.get,
        'headers': {},
        # 'queryParams': r'^from=A\d+&to=A\d+$',
        'data': []
    }
]

methodMatcher = {
    'CREATE': {
        'uris': createUrls,
        'data': True
    },
    'MODIFY': {
        'uris': modifyUrls,
        'headers': {
            'content-type': 'application/json'
        },
        'data': True
    },
    'FETCH': {
        'uris': fetchUrls,
        'headers': [],
        'data': False
    }
}
