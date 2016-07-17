import sys
import time
import json
#from sense_hat import SenseHat
from iota import iota

class weathernode:
	def __init__(self, seed, temperature=None, humidity=None, pressure=None, senseHAT=True):
		if senseHAT==False:
			self.sense=None
			if temperature!=None:
				self.temperature=temperature
			if humidity!=None:
				self.humidity=humidity
			if pressure!=None:
				self.pressure=pressure
		else:
			self.sense=SenseHat()
		self.node=iota(seed)
		self.txCounter=self.node.txCounter
	
	def run(self):
		while True:
			try:
				print("Waiting until the Weatehr Node reciving a request...")
				self.txCounter=self.node.txCounter
				while True:
					self.transaction=self.node.searchNewTransaction()
					if self.txCounter!=self.node.txCounter:
						break
					time.sleep(5)
				while True:
					self.persistence=self.node.checkConformation(self.transaction)
					if self.presistence==100:
						break
					time.sleep(5)
				self.message=self.node.searchMessage(self.transaction)
				print(self.message)
				self.message=self.message.replace('\'','\"')
				self.jsonData=json.loads(self.message)
				self.execute(self.jsonData)
			except Exception as e:
				print("Can not run Weather Node. "+str(e))
				return None

	def execute(self, jsonData):
		try:
			if self.jsonData['command']=="getWeather" :
				print("Weather request recived.")
				if self.sense!=None:
					self.message=readWeather()
				else:
					self.message="{'Temperature':'"+self.temperature+"', 'Humidity':'"+self.humidity+"','Pressure':'"+self.pressure+"'}"
				self.responsAdress=self.jsonData['address']
				self.node.sendMessage(self.responsAdress, self.message, '0')
				print("Succesfully send Weather Infos back to:"+responsAdress)
			elif jsonData['command']=="sendPromotion":
				print("Promotion request recived.")
				if self.sense!=None:
					print("Promotion Text:"+jsonData['promotion'])
					scrollText(jsonData['promotion'])
				else:
					print("Promotion Text:"+jsonData['promotion'])
			else:
				print("Can't read sucessfully a command."+jsonData)
		except Exception as e:
			self.error="Can't execute command. "+str(e)
			return None

	def readWeather(self):
		self.temperature = self.sense.temperature()
		self.humidity = self.sense.get_humidity()
		self.pressure = self.sense.get_pressure()
		return "{'Temperature':'"+str(self.temperature)+"', 'Humidity':'"+str(self.humidity)+"','Pressure':'"+str(self.pressure)+"'}"


	def scrollText(self,message):
		self.sense.show_message(message,text_colour=[255, 0, 0])


