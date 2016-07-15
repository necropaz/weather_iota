import sys
import time
import json
from iota import iota

class weatherclient:
	def __init__(self, seed, address):
		self.seed=seed
		self.address=address
		self.node=iota(seed)
		self.txCounter=self.node.txCounter
	
	def requestWeather(self, respondAddress):
		message="{'command':'getWeather','address':'"+respondAddress+"'}"
		try:
			self.node.sendMessage(self.seed, self.address, self.message, '1')
			print("Weather Node is Running.")
			print("Waiting until the Weatehr Node recived a request.")
			self.txCounter=self.node.txCounter
			while True:
				time.sleep(5)
				self.transaction=self.node.searchNewTransaction()
				if self.txCounter+2==self.node.txCounter:
					break
			self.message=self.node.searchMessage(transaction).replace('\'','\"')
			self.jsonData=json.loads(self.message)
			execute(self.jsonData)
		except Exception as e:
			self.error="Can not run Weather Node. "+str(e)
			return None

	def sendPromotion(self, message):
		message="{'command':'sendPromotion','promotion':'"+message+"'}"
		try:
			self.node.sendMessage(self.seed, self.address, self.message, '1')
			print("Succesfully send Promotion.")
		except Exception as e:
			self.error="Can not send a Promotion. " +str(e)
			return None


	def execute(self, jsonData):
		try:
			print("Temperatur: "+jsonData['temperature']+"Humidity: "+jsonData['humidity']+"Pressure: "+jsonData['pressure'])
		except Exception as e:
			self.error="Can't execute command. "+str(e)
			return None

	
