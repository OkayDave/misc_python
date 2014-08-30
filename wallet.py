#!/usr/bin/env python

import subprocess
import sys

keys = {
  "doge": "dogecoind",
  "lite": "litecoind",
  "digi": "digibyted",
  "vert": "vertcoind",
  "redd": "reddcoind"
  }

balance = float(subprocess.check_output(keys[str(sys.argv[1])] + " getbalance",shell=True))
print("{:,.2f}".format(balance))
