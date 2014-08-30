#!/usr/bin/env python

import requests
#import random
import json
import textwrap

mashape_key = ""

url = "https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous"
headers = {"X-Mashape-Authorization": mashape_key}

r =  requests.get(url, headers=headers)
data = json.loads(r.text)

q = textwrap.fill(data["quote"], width=25)
a = "${color3}"+data["author"]+"${color}"


formatted = "\"" + q + "\"\n\n" + a

print (formatted)

