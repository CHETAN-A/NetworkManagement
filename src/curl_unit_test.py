
testcases = [

{
    "info": "Create Device API : Adding A1 into network",
    "command" : "curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices\n\
        content-type : application/json\n\
        \n\
        {\"type\" : \"COMPUTER\", \"name\" : \"A1\"}'"
},

{
    "info": "Create Device API : Adding A2 into network",
    "command" : "curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices\n\
        content-type : application/json\n\
        \n\
        {\"type\" : \"COMPUTER\", \"name\" : \"A2\"}'"
},

{
    "info": "Create Device API  : Adding A3 into network",
    "command" : "curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices\n\
        content-type : application/json\n\
        \n\
        {\"type\" : \"COMPUTER\", \"name\" : \"A3\"}'"
},

{
    "info": "Create Device API  : Adding A4 into network",
    "command" : "curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices\n\
content-type : application/json\n\
\n\
{\"type\" : \"COMPUTER\", \"name\" : \"A4\"}'"
},

{
    "info": "Create Device API  : Adding A5 into network",
    "command" : "curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices\n\
content-type : application/json\n\
\n\
{\"type\" : \"COMPUTER\", \"name\" : \"A5\"}'"
},

{
    "info": "Create Device API ",
    "command" : "curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices\n\
content-type : application/json\n\
\n\
{\"type\" : \"REPEATER\", \"name\" : \"R1\"}'"
},

{
    "info": "Create Device API ",
    "command" : "curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices\n\
content-type : application/json\n\
\n\
{\"type\" : \"COMPUTER\", \"name\" : \"A6\"}'"
},


{
    "info": "Create Device API : Invalid Device Name error",
    "command" : "curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices\n\
content-type : application/json\n\
\n\
{\"type\" : \"COMPUTER\", \"name\" : \"1A1\"}'"
},


{
    "info": "Create Device API : Request Duplicate Data Error",
    "command" : 
"curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices\n\
content-type : application/json\n\
app : text/asd\n\
\n\
{\"type\" : \"COMPUTER\", \"name\" : \"A1\"\n\
, \"device\": \"Sdff\"}'"
},

{
    "info": "Create Device API : Request Device Type Error",
    "command" : 
"curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices\n\
content-type : application/json\n\
app : text/asd\n\
\n\
{\"type\" : \"COMPUTERR\", \"name\" : \"A1\"\n\
, \"device\": \"Sdff\"}'"
},

{
    "info": "Create Device API : Request Data Error",
    "command" : 
"curl --request  POST \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /devices'"
},


{
    "info": "MODIFY API",
    "command" : 
"curl --request POST  --url http://localhost:8080/ajiranet/process\
 --data 'MODIFY /devices/A1/strength\n\
content-type : application/json\n\
app : text/asd\n\
\n\
{\"value\": 6}'"
},


{
    "info": "MODIFY API : Wrong device Value Error ",
    "command" : 
"curl --request POST  --url http://localhost:8080/ajiranet/process\
 --data 'MODIFY /devices/A1/strength\n\
content-type : application/json\n\
app : text/asd\n\
\n\
{\"value\": \"Helloworld\"}'"
},

{
    "info": "MODIFY API : Wrong device name Error ",
    "command" : 
"curl --request POST  --url http://localhost:8080/ajiranet/process\
 --data 'MODIFY /devices/M1/strength\n\
content-type : application/json\n\
app : text/asd\n\
\n\
{\"value\": 6}'"
},

{
    "info": "MODIFY API : Data error",
    "command" : 
"curl --request POST  --url http://localhost:8080/ajiranet/process\
 --data 'MODIFY /devices/M1/strength\n\
content-type : application/json\n\
app : text/asd'"
},


{
    "info": "Create Connection : proper connection",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"A1\", \"targets\": [\"A2\"]}'"
},


{
    "info": "Create Connection : Command Error",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"R1\"}'"
},


{
    "info": "Create Connection : Invalid Source",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : [], \"targets\": [\"A2\"]}'"
},


{
    "info": "Create Connection : invalid source pattern",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"1a\", \"targets\": [\"A2\"]}'"
},


{
    "info": "Create Connection : unexisting source",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"X1\", \"targets\": [\"A2\"]}'"
},


{
    "info": "Create Connection : invalid target node",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"A1\", \"targets\": [\"A2\",7]}'"
},


{
    "info": "Create Connection : invalid target pattern",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"A1\", \"targets\": [\"A2\", \"4R\"]}'"
},


{
    "info": "Create Connection : unexisting target node",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"A1\", \"targets\": [\"A4\", \"A9\"]}'"
},


{
    "info": "Create Connection : invalid connection to same device",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"A1\", \"targets\": [\"A1\"]}'"
},


{
    "info": "Create Connection : Device already connected error",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"A1\", \"targets\": [\"A2\"]}'"
},


{
    "info": "Create Connection : proper connection",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"A1\", \"targets\": [\"A3\"]}'"
},

{
    "info": "Create Connection : proper connection",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"A5\", \"targets\": [\"A4\"]}'"
},

{
    "info": "Create Connection : proper connection",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"R1\", \"targets\": [\"A2\"]}'"
},

{
    "info": "Create Connection : proper connection",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"R1\", \"targets\": [\"A5\"]}'"
},

{
    "info": "Create Connection : proper connection",
    "command" : 
"curl --request POST   \
--url http://localhost:8080/ajiranet/process \
--data 'CREATE /connections \n\
content-type : application/json\n \
\n\
{\"source\" : \"A2\", \"targets\": [\"A4\"]}'"
},


{
    "info": "FETCH routes",
    "command" : "curl --request POST  \
--url http://localhost:8080/ajiranet/process \
--data 'FETCH /info-routes?from=A1&to=A4'"
},


{
    "info": "FETCH routes",
    "command" : "curl --request POST  \
--url http://localhost:8080/ajiranet/process \
--data 'FETCH /info-routes?from=A1&to=A5'"
},

{
    "info": "FETCH routes",
    "command" : "curl --request POST  \
--url http://localhost:8080/ajiranet/process \
--data 'FETCH /info-routes?from=A4&to=A3'"
},


{
    "info": "FETCH routes",
    "command" : "curl --request POST  \
--url http://localhost:8080/ajiranet/process \
--data 'FETCH /info-routes?from=A1&to=A1'"
},


{
    "info": "FETCH routes : no route",
    "command" : "curl --request POST  \
--url http://localhost:8080/ajiranet/process \
--data 'FETCH /info-routes?from=A1&to=A6'"
},


{
    "info": "FETCH routes : invalid command",
    "command" : "curl --request POST  \
--url http://localhost:8080/ajiranet/process \
--data 'FETCH /info-routes?from=A2&to=R1'"
},


{
    "info": "FETCH routes : invalid command",
    "command" : "curl --request POST  \
--url http://localhost:8080/ajiranet/process \
--data 'FETCH /info-routes?from=A3'"
},

{
    "info": "FETCH routes : invalid command",
    "command" : "curl --request POST  \
--url http://localhost:8080/ajiranet/process \
--data 'FETCH /info-routes'"
},


{
    "info": "FETCH routes : non-existing target node",
    "command" : "curl --request POST  \
--url http://localhost:8080/ajiranet/process \
--data 'FETCH /info-routes?from=A1&to=A10'"
},

{
    "info" : "FETCH Device List",
    "command": "curl --request POST  \
--url http://localhost:8080/ajiranet/process \
--data 'FETCH /devices'"
}

]

import os
import time

for testcase in testcases:
    print("\n-----------------------------------------\n\n")
    
    print(testcase['info'], end="\n\n")
    os.system('echo "## {}\n\n" >> testcases.md'.format(testcase['info']))
    print('Command: \n' + testcase['command'], end="\n\n")
    os.system('echo "{}\n\n" >> testcases.md '.format(testcase['command']))
    os.system(testcase['command'])
    
    print("\n-----------------------------------------\n\n")
    time.sleep(3)