from .view import Connections, Devices, Routes

device = Devices()
connection = Connections()
route = Routes()

createUrls = [
    {
        'uri' : r'^/devices$',
        'view': device.post,
        'headers': {
            'content-type': ['application/json', 'application/x-www-form-urlencoded']
        },
        'data': ['type', 'name']
    },
    {
        'uri' : r'^/connections$',
        'view': connection.post,
        'headers': {
            'content-type': ['application/json', 'application/x-www-form-urlencoded']
        },
        'data': ['source', 'targets']
    }
]

modifyUrls = [
    {
        'uri' : r'^/devices/(?P<name>[A-Za-z_]\w+)/(?P<modifier>[A-Za-z_]+)$',
        'view': device.put,
        'headers': {
            'content-type': ['application/json', 'application/x-www-form-urlencoded']
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
            'content-type': ['application/json', 'application/x-www-form-urlencoded']
        },
        'data': True
    },
    'FETCH': {
        'uris': fetchUrls,
        'headers': [],
        'data': False
    }
}
