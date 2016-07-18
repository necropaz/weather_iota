import sys
import json
import time
import os

from weather_iota import weathernode

#Enter here your seed.
seed=raw_input("Enter the seed of the IOTA Weather Node? ")

weather=weathernode(seed, temperature="32",humidity="50",pressure="1013", senseHAT=False)
weather.run()
print("End Iota Weather Node!")
