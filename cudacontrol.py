#!/usr/bin/env python

import subprocess
import time
import random

def get_temp():
  output = subprocess.check_output(" nvidia-smi | grep Default | cut -d' ' -f5", shell=True)
  temp = float(output.strip().decode("utf-8")[0:-1])
  print("tmp: " + str(temp))
  return temp

def start_miner():
  cmd = random.choice(cmds)
  print("starting miner: " + cmd)
  return subprocess.Popen(cmd, shell=True)

def stop_miner():

  return True

cmds = [

  "cudaminer -o stratum+tcp://doge-stratum.nimblecoin.us:3333 -u  -p "

  ]
isRunning = False
count = 0
process = None;

while True:
  if isRunning:
    if (get_temp() > 85):
      process.terminate()
      isRunning = False
      time.sleep(90)
    if count >= 540: # 90 minutes
      print("switching shit up")
      process.terminate()
      isRunning = False
      time.sleep(15)
      count = 0

  else:
    if (get_temp() < 70):
      process = start_miner()
      isRunning = True

  time.sleep(10)
  count += 1

  


