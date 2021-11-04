# pip install dht11

import RPi.GPIO as GPIO
import dht11
import time
import datetime

class DHT:

	# def Logs(self, temperature, humidity):
	# 	f = open("Logs\Logs.txt", "a", encoding="UTF-8")

	def Data(self):
		# initialize GPIO
		GPIO.setwarnings(True)
		GPIO.setmode(GPIO.BCM)

		# read data using pin 14
		instance = dht11.DHT11(pin=14)

		try:
			result = instance.read()
			if (result.is_valid()):
				temperature = result.temperature
				humidity = result.humidity
				# DHT11.Logs(temperature, humidity)
				return temperature, humidity

		except KeyboardInterrupt:
			print("Cleanup")
			GPIO.cleanup()

	# def __init__(self):
	# 	DHT11.Data()
