#!/usr/bin/python
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

jsondata = json.dumps(data)
print(jsondata)
print(json.loads(jsondata))
print(json.loads(jsondata)[0]['b'])

