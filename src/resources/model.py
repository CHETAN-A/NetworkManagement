
device_name_regex = r'^[A-Za-z_]\w+$'

class NetworkDeviceManager:
    def __init__(self):
        super().__init__()
        self.nodes = {}

    def addNode(self, name, nodeType):
        self.nodes[name] = {
            'type': nodeType,
            'strength': 0,
            'connections': set()
        }

    def isNodePresent(self, name):
        if name in self.nodes:
            return True
        return False

    def isNodeOfType(self, node, nodeType):
        if self.nodes[node]['type'] == nodeType:
            return True
        return False

    def getNodes(self):
        nodesList = []
        for node in self.nodes.keys():
            nodesList.append({
                'type': self.nodes[node]['type'],
                'name': node
            })
        return nodesList

    def addConnection(self, node1, node2):
        self.nodes[node1]['connections'].add(node2)
        self.nodes[node2]['connections'].add(node1)

    def areNodesConnected(self, node1, node2):
        if node1 in self.nodes[node2]['connections']:
            return True
        return False

    def updateStrength(self, node, value):
        self.nodes[node]['strength'] = value

    def findRoute(self, source, target):
        # print(('source', source), ('target', target))
        if source == target:
            return [source, target]

        distance = {}
        predecessor = {}

        routeFound = False
        path = []

        for node in self.nodes.keys():
            distance[node] = float('inf')
            predecessor[node] = -1

        distance[source] = 0
        visitedNodes = set()

        noOfNodesVisited = 0
        while noOfNodesVisited < len(self.nodes.keys())-1:
            node = getMinDistanceNode(distance, visitedNodes)
            visitedNodes.add(node)

            if node == target:
                routeFound = True
                break

            for adjacentNode in self.nodes[node]['connections']:
                if adjacentNode not in visitedNodes:
                    if self.nodes[adjacentNode]['type'] == 'REPEATER':
                        if distance[adjacentNode] > distance[node] + 1:
                            distance[adjacentNode] = distance[node] + 1
                            predecessor[adjacentNode] = node
                    elif distance[adjacentNode] > distance[node] + 2:
                        distance[adjacentNode] = distance[node] + 2
                        predecessor[adjacentNode] = node
            noOfNodesVisited += 1

        if routeFound:
            path.append(target)
            traverser = target
            while predecessor[traverser] != -1:
                path.insert(0, predecessor[traverser])
                traverser = predecessor[traverser]

        return path


def getMinDistanceNode(distance, visitedNodes):
    minDistanceNode = None
    for node in distance.keys():
        if node not in visitedNodes:
            if not minDistanceNode:
                minDistanceNode = node
            elif distance[node] < distance[minDistanceNode]:
                minDistanceNode = node
    return minDistanceNode
