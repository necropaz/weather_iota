import sys
import json
import time
import os
from weather_iota import weatherclient

address=raw_input("The address of the Weather Node? ")
seed=raw_input("The seed of you Weather Client? ")
char=raw_input("If you will send a weather request tip w, if you wanna send a promotion tip p.? [w/p]? ")

client=weatherclient(seed, address)

if char=='w':
	client.requestWeather()

elif char=='p':
	message=raw_input("What for a promotion you wanna send? ")
	client.sendPromotion(message)

else:
	print("Your Input is not [r/p]")



