## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  -H Content-Type: text/plain --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST  -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST -H Content-Type: text/plain  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


## Create Device API : Adding A1 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A1}'


## Create Device API : Adding A2 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A2}'


## Create Device API  : Adding A3 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
        content-type : application/json
        
        {type : COMPUTER, name : A3}'


## Create Device API  : Adding A4 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A4}'


## Create Device API  : Adding A5 into network


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A5}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : REPEATER, name : R1}'


## Create Device API 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : A6}'


## Create Device API : Invalid Device Name error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json

{type : COMPUTER, name : 1A1}'


## Create Device API : Request Duplicate Data Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTER, name : A1
, device: Sdff}'


## Create Device API : Request Device Type Error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'CREATE /devices
content-type : application/json
app : text/asd

{type : COMPUTERR, name : A1
, device: Sdff}'


## Create Device API : Request Data Error


curl --request  POST --url http://localhost:8080/ajiranet/process --data 'CREATE /devices'


## MODIFY API


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Wrong device Value Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/A1/strength
content-type : application/json
app : text/asd

{value: Helloworld}'


## MODIFY API : Wrong device name Error 


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd

{value: 6}'


## MODIFY API : Data error


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'MODIFY /devices/M1/strength
content-type : application/json
app : text/asd'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : Command Error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1}'


## Create Connection : Invalid Source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : [], targets: [A2]}'


## Create Connection : invalid source pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : 1a, targets: [A2]}'


## Create Connection : unexisting source


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : X1, targets: [A2]}'


## Create Connection : invalid target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2,7]}'


## Create Connection : invalid target pattern


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2, 4R]}'


## Create Connection : unexisting target node


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A4, A9]}'


## Create Connection : invalid connection to same device


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A1]}'


## Create Connection : Device already connected error


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A1, targets: [A3]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A5, targets: [A4]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A2]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : R1, targets: [A5]}'


## Create Connection : proper connection


curl --request POST   --url http://localhost:8080/ajiranet/process --data 'CREATE /connections 
content-type : application/json
 
{source : A2, targets: [A4]}'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A4'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A5'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A4&to=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A6'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A2&to=R1'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A3'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes'


## FETCH routes


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /info-routes?from=A1&to=A10'


## FETCH Device List


curl --request POST  --url http://localhost:8080/ajiranet/process --data 'FETCH /devices'


