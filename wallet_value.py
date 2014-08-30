#!/usr/bin/env python

import subprocess
import sys
import requests
import json

def eur_to_gbp(euros):
  endpoint = "http://openexchangerates.org/api/latest.json?app_id=77e28cca29a347d9bf0abd8c1c3d7a6d"

  req = requests.get(endpoint)
  data = json.loads(req.text)

  eur = float(data["rates"]["EUR"])
  gbp = float(data["rates"]["GBP"])


  dollars = euros / eur
  #print(dollars)
  pounds = dollars * gbp 
  #print(pounds)
  return pounds

def btc_to_gbp(btc):
  endpoint = "http://api.coindesk.com/v1/bpi/currentprice/GBP.json"

  req = requests.get(endpoint)
  data = json.loads(req.text)

  one_btc = float(data["bpi"]["GBP"]["rate"])
  return btc*one_btc


keys = {
  "doge": {
    "cmd":"dogecoind getbalance",
    "pair":"EURXDG",
    "cryptsyid": "132",
    "cryptsysym": "DOGE",
    "result":"ZEURXXDG",
    "method":"div"
    },

  "lite": { 
    "cmd":"litecoind getbalance",
    "pair":"LTCEUR",
    "result":"XLTCZEUR",
    "method":"mul"
    },

  "btc": {
    "cmd":"python ~/python/btc_balance.py",
    "pair":"BTCEUR",
    "result":"XXBTZEUR",
    "method":"mul"
  },


  "vert": { 
    "cmd":"vertcoind getbalance",
    "cryptsyid":"151",
    "cryptsysym": "VTC",
    "result":"XLTCZEUR",
    "method":"mul"
    },

  "digi": {
    "cmd": "digibyted getbalance",
    "cryptsyid": "167",
    "cryptsysym": "DGB"
  },

  "redd": {
    "cmd": "reddcoind getbalance",
    "cryptsyid": "126",
    "cryptsysym": "RDD"
  }

  }

balance = 0.0
currency = str(sys.argv[1])
coin_balance = float(subprocess.check_output(keys[currency]["cmd"] ,shell=True))


if(currency == "lite" or currency =="btc"):
  url = "https://api.kraken.com/0/public/Ticker?pair="+keys[currency]["pair"]

  req = requests.get(url)
  data = json.loads(req.text)

  euro_rate = float(data["result"][keys[currency]["result"]]["p"][0])

  #print("euro_rate " + str(euro_rate))

  if keys[currency]["method"]=="mul":
    euro_balance = coin_balance*euro_rate
  else:
    euro_balance = coin_balance/euro_rate

  #print("euro_balance " + str(euro_balance))
  balance = eur_to_gbp(euro_balance)

if(currency == "vert" or currency=="doge" or currency=="digi" or currency=="redd"):
  url = "http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid="+keys[currency]["cryptsyid"]

  req = requests.get(url)
  data = json.loads(req.text)
 
  btc_price = float(data["return"]["markets"][keys[currency]["cryptsysym"]]["lasttradeprice"])

  btc_balance = btc_price*coin_balance
  balance = btc_to_gbp(btc_balance)

print(u"\u00A3"+"{:,.2f}".format(balance))

