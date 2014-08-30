#!/usr/bin/env python

import glob
import random
import os

wallpaper_folder = ""

files = glob.glob(wallpaper_folder)
random.shuffle(files)
command = "feh --no-fehbg --bg-fill " + files[0] + " " + files[1]  

os.system(command)

