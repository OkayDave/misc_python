#!/usr/bin/env python

import xml.etree.ElementTree as ET
import sys
import datetime

def code_image(code, height, width, x, y):
	path = "/home/dave/.config/conky/icons/%s.png" % code
	op = "image {} -p {},{} -s {}x{}".format(path, x, y, height, width)
	op = "${"+op+"}"
	return op

def temp(temp):
	return temp +"°"

today = datetime.date.today().strftime("%d %b %Y")

x_offset = int(sys.argv[1])
y_offset = int(sys.argv[2])
func 	 = sys.argv[3]

WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

tree = ET.parse("/home/dave/.cache/weather.xml")
root = tree.getroot()

condition_xml = root.find("channel/item/{%s}condition" % WEATHER_NS)
condition = {}
condition["condition"] = condition_xml.get("text")
condition["code"] = condition_xml.get("code")
condition["temp"] = condition_xml.get("temp")


forecasts_xml = root.findall("channel/item/{%s}forecast" % WEATHER_NS)

forecasts = []
for day in forecasts_xml:
	forecasts.append({
		"date": day.get("date"),
		"day": day.get("day"),
		"low": day.get("low"),
		"high": day.get("high"),
		"condition": day.get("text"),
		"code": day.get("code")
		})

	if day.get("date") == today: 
		condition["low"] = day.get("low")
		condition["high"] = day.get("high")


if func=="condition":
	x_offset = 0
	op_condition =  "${offset 67}${voffset -10}${font Ubuntu Sans:size=20}" +condition["condition"] +"${font Ubuntu Sans:size9}\n"
	op_condition += "${offset 67}${voffset 12}${font Ubuntu Sans:size=13}" + temp(condition["temp"]) +"${font}"   #\n"
	op_condition += "${alignr}${color1}" + temp(condition["low"])+" ${color2}"+temp(condition["high"])+" "
	op_images = code_image(condition["code"], 50, 50, x_offset+5, y_offset+20) 

	output = op_images + op_condition
else:
	op_forecasts =  "\n${font Ubuntu Mono:size=8}\n"
	#op_forecasts += "{} $alignc {} $alignr {}\n\n\n".format(forecasts[1]["day"], forecasts[2]["day"], forecasts[3]["day"])

	op_images = "\n"
	
	#op_images += code_image(forecasts[0]["code"], 32, 32, x_offset-10, y_offset) + "\n"
	#op_images += code_image(forecasts[1]["code"], 32, 32, x_offset+40, y_offset) + "\n"
	#op_images += code_image(forecasts[2]["code"], 32, 32, x_offset+90, y_offset) + "\n"
	#op_images += code_image(forecasts[3]["code"], 32, 32, x_offset+140, y_offset) + "\n"
	#op_images += code_image(forecasts[5]["code"], 32, 32, x_offset+130, y_offset) + "\n"
	
	i = 0
	for fc in forecasts:
		op_images += code_image(fc["code"], 32, 32, x_offset+(i*40), y_offset) #+ "\n"
		i+=1

	output = op_forecasts + op_images



#output = op_condition + "" + op_images #+ "${font}${color}"

print(output)