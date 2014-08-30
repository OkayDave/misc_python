#!/usr/bin/env python
import requests
import json

wallet_public_key = ""

r = requests.get("http://blockchain.info/address/"+wallet_public_key+"?format=json")

j = json.loads(r.text)

output = "{:,.8f}".format(j["final_balance"]/100000000)

print(output)
