#!/usr/bin/env python

import sys

f = open("/home/dave/.cache/nowplaying", "w")
f.write(sys.argv[1])
f.close()