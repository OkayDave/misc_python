#!/usr/bin/env python

import requests
import json

user = "" # BitMinter username
key = "" # BitMinter API key

r = requests.get("http://bitminter.com/api/users/"+user+"/?key="+key)
data = json.loads(r.text)
output = data["hash_rate"] + " MH/s (" + str(data["balances"]["BTC"]) + ")"
print(output)  