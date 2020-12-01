import unittest
testcases = [
    {
        "command": "CREATE /devices\n        content-type : application/json\n        \n        {\"type\" : \"COMPUTER\", \"name\" : \"A1\"}",
        "response": {
            "msg": "Successfully added A1"
        },
        "status": 200
    },
    {
        "command": "CREATE /devices\n        content-type : application/json\n        \n        {\"type\" : \"COMPUTER\", \"name\" : \"A2\"}",
        "response": {
            "msg": "Successfully added A2"
        },
        "status": 200
    },
    {
        "command": "CREATE /devices\n        content-type : application/json\n        \n        {\"type\" : \"COMPUTER\", \"name\" : \"A3\"}",
        "response": {
            "msg": "Successfully added A3"
        },
        "status": 200
    },
    {
        "command": "CREATE /devices\ncontent-type : application/json\n\n{\"type\" : \"COMPUTER\", \"name\" : \"A4\"}",
        "response": {
            "msg": "Successfully added A4"
        },
        "status": 200
    },
    {
        "command": "CREATE /devices\ncontent-type : application/json\n\n{\"type\" : \"COMPUTER\", \"name\" : \"A5\"}",
        "response": {
            "msg": "Successfully added A5"
        },
        "status": 200
    },
    {
        "command": "CREATE /devices\ncontent-type : application/json\n\n{\"type\" : \"REPEATER\", \"name\" : \"R1\"}",
        "response": {
            "msg": "Successfully added R1"
        },
        "status": 200
    },
    {
        "command": "CREATE /devices\ncontent-type : application/json\n\n{\"type\" : \"COMPUTER\", \"name\" : \"A6\"}",
        "response": {
            "msg": "Successfully added A6"
        },
        "status": 200
    },
    {
        "command": "CREATE /devic\ncontent-type : application/json\n\n{\"type\" : \"COMPUTER\", \"name\" : \"A6\"}",
        "response": {
            "msg": "Invalid Command"
        },
        "status": 400
    },
    {
        "command": "CREATE /devices\ncontent-type : application/json\n\n{\"type\" : \"COMPUTER\", \"name\" : \"1A1\"}",
        "response": {
            "msg": "Device '1A1' name is not valid"
        },
        "status": 400
    },
    {
        "command": "CREATE /devices\ncontent-type : application/json\napp : text/asd\n\n{\"type\" : \"COMPUTER\", \"name\" : \"A1\"\n, \"device\": \"Sdff\"}",
        "response": {
            "msg": "Device 'A1' already exists"
        },
        "status": 400
    },
    {
        "command": "CREATE /devices\ncontent-type : application/json\napp : text/asd\n\n{\"type\" : \"COMPUTERR\", \"name\" : \"A1\"\n, \"device\": \"Sdff\"}",
        "response": {
            "msg": "type 'COMPUTERR' is not supported"
        },
        "status": 400
    },
    {
        "command": "CREATE /devices",
        "response": {
            "msg": "Invalid Command"
        },
        "status": 400
    },
    {
        "command": "MODIFY /devices/A1/strength\ncontent-type : application/json\napp : text/asd\n\n{\"value\": 6}",
        "response": {
            "msg": "Successfully defined strength"
        },
        "status": 200
    },
    {
        "command": "MODIFY /devices/A1/strength\ncontent-type : application/json\napp : text/asd\n\n{\"value\": \"Helloworld\"}",
        "response": {
            "msg": "value should be an +ve integer"
        },
        "status": 400
    },
    {
        "command": "MODIFY /devices/M1/strength\ncontent-type : application/json\napp : text/asd\n\n{\"value\": 6}",
        "response": {
            "msg": "Device 'M1' not found"
        },
        "status": 400
    },
    {
        "command": "MODIFY /devices/M1/strength\ncontent-type : application/json\napp : text/asd",
        "response": {
            "msg": "Invalid Command"
        },
        "status": 400
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"A1\", \"targets\": [\"A2\"]}",
        "response": {
            "msg": "Successfully Connected"
        },
        "status": 200
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"R1\"}",
        "response": {
            "msg": "Invalid Command"
        },
        "status": 400
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : [], \"targets\": [\"A2\"]}",
        "response": {
            "msg": "Device '[]' name is not valid"
        },
        "status": 400
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"1a\", \"targets\": [\"A2\"]}",
        "response": {
            "msg": "Device '1a' name is not valid"
        },
        "status": 400
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"X1\", \"targets\": [\"A2\"]}",
        "response": {
            "msg": "Device 'X1' not found"
        },
        "status": 400
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"A1\", \"targets\": [\"A2\",7]}",
        "response": {
            "msg": "Device '7' name is not valid"
        },
        "status": 400
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"A1\", \"targets\": [\"A2\", \"4R\"]}",
        "response": {
            "msg": "Device '4R' name is not valid"
        },
        "status": 400
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"A1\", \"targets\": [\"A4\", \"A9\"]}",
        "response": {
            "msg": "Device 'A9' not found"
        },
        "status": 400
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"A1\", \"targets\": [\"A1\"]}",
        "response": {
            "msg": "Cannot connect device to itself"
        },
        "status": 400
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"A1\", \"targets\": [\"A2\"]}",
        "response": {
            "msg": "Devices A1 and A2 are already connected"
        },
        "status": 400
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"A1\", \"targets\": [\"A3\"]}",
        "response": {
            "msg": "Successfully Connected"
        },
        "status": 200
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"A5\", \"targets\": [\"A4\"]}",
        "response": {
            "msg": "Successfully Connected"
        },
        "status": 200
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"R1\", \"targets\": [\"A2\"]}",
        "response": {
            "msg": "Successfully Connected"
        },
        "status": 200
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"R1\", \"targets\": [\"A5\"]}",
        "response": {
            "msg": "Successfully Connected"
        },
        "status": 200
    },
    {
        "command": "CREATE /connections \ncontent-type : application/json\n \n{\"source\" : \"A2\", \"targets\": [\"A4\"]}",
        "response": {
            "msg": "Successfully Connected"
        },
        "status": 200
    },
    {
        "command": "FETCH /info-routes?from=A1&to=A4",
        "response": {
            "msg": "Route is A1->A2->A4"
        },
        "status": 200
    },
    {
        "command": "FETCH /info-routes?from=A1&to=A5",
        "response": {
            "msg": "Route is A1->A2->R1->A5"
        },
        "status": 200
    },
    {
        "command": "FETCH /info-routes?from=A4&to=A3",
        "response": {
            "msg": "Route is A4->A2->A1->A3"
        },
        "status": 200
    },
    {
        "command": "FETCH /info-routes?from=A1&to=A1",
        "response": {
            "msg": "Route is A1->A1"
        },
        "status": 200
    },
    {
        "command": "FETCH /info-routes?from=A1&to=A6",
        "response": {
            "msg": "Route not found"
        },
        "status": 400
    },
    {
        "command": "FETCH /info-routes?from=A2&to=R1",
        "response": {
            "msg": "Route cannot be calculated with repeater"
        },
        "status": 400
    },
    {
        "command": "FETCH /info-routes?from=A3",
        "response": {
            "msg": "Invalid Request"
        },
        "status": 400
    },
    {
        "command": "FETCH /info-routes",
        "response": {
            "msg": "Invalid Request"
        },
        "status": 400
    },
    {
        "command": "FETCH /info-routes?from=A1&to=A10",
        "response": {
            "msg": "Device 'A10' not found"
        },
        "status": 400
    },
    {
        "command": "FETCH /devices",
        "response": {
            "devices": [
                {
                    "type": "COMPUTER",
                    "name": "A1"
                },
                {
                    "type": "COMPUTER",
                    "name": "A2"
                },
                {
                    "type": "COMPUTER",
                    "name": "A3"
                },
                {
                    "type": "COMPUTER",
                    "name": "A4"
                },
                {
                    "type": "COMPUTER",
                    "name": "A5"
                },
                {
                    "type": "REPEATER",
                    "name": "R1"
                },
                {
                    "type": "COMPUTER",
                    "name": "A6"
                }
            ]
        },
        "status": 200
    }
]

import requests

class TestAjiraNetwork(unittest.TestCase):
    def test_all(self):
        for testcase in testcases:
            response = requests.post('http://localhost:8080/ajiranet/process', data=testcase['command'])
            # print(response.status_code)
            # print(response.json())
            self.assertEqual(response.status_code, testcase['status'])
            self.assertDictEqual(response.json(), testcase['response'])

if __name__ == '__main__':
    unittest.main()