from ezsc import ezscApplication
import asyncio 
import os 
import logging 
from aiohttp import web
import json
import time
import thereading
from db_connector import Connector
#from security import Encryption
#from security import Decryption

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

connector_app = Connector()
ezsc_controller = ezscApplication()
# A function that will allow devices to join the network

class SHA: # *******SHA = Secure Home Automation **************
	'''@staticmethod 
	async def permit_join(): # why request? 
		await LOGGER.info("Permitting devices to join the network for the next 60s ...")
		permit_join_future = asyncio.create_task(ezsc_controller.permit_join())
		await permit_join_future.add_done_callback(lambda futre: LOGGER.info("devices can no longer join the network"))'''

	#*** A FUNCTION THAT HELPS GETS THE DEVICES ***** 
	@staticmethod
	async def _get_devices():  
		return  ezsc_controller.get_devices()

	#*** A DAEMON THREAD TO CHECK FOR NEW DEVICES ********   
	@staticmethod 
	def thread_check_for_new_devices():
		LOGGER.info("STARING THE THREAD FOR CHECKING FOR NEW DEVICES THREAD")
		devices = asyncio.run(SHA._get_devices())

		# Check if the devices is in the database ( will need to decrypt the existing devies in the database and compare them | or compare the hashes )
		for i in range(len(devices)):
			_device = devices[i]
			_device_ieee = _device["ieee"]
			# encrypt the _ieee
			#Encryption.encrypt_data(_ieee)
		try:
			#check if the encrypted _ieee is already in the database
			rval = check_if_device_exists(_ieee) 
			if rval == False:
				connector_app.insertIEEE(_ieee)

		except Exception as er:
			LOGGER.exception("Failed to insert")

		LOGGER.info("DEAMON FOR CHECKING FOR NEW DEVICES IS COMPLETED") 

	# A THREAD THAT LISTENS FOR CHANGES IN THE ACTION COLUMN 
	@staticmethod
	def thread_listen_for_action():
		dict_devices{} # dictionary for the devices
		LOGGER.info("STARTING THREAD THAT LISTENS FOR ACTIONS")
		
		_ieee_list, action_list = connector_app.qyery_iee_and_action()
		
		# *** insert the ieee's as keys and actions as values *******
		for i in range(len(_ieee_list)):
			dict_devices{_ieee_list[i] : action_list[i]}

		# perform the action fro all devices 
		for key in dict_devices:
			SHA.control_devic(key, dict_devices[key]) # send the ieee and the action to perform that action for the specific device

		# empty list and repeat
	#******** A FUNCTION TO CONTROLL THE DEVICE ********
	@staticmethod
	async def control_device(device, command):
		device_ieee = device["ieee"]
		
		try:
			await ezsc_controller.send_command(device_ieee, command, "")
		except Exception as e:
			LOGGER.exception("Failed to control device!")
	
	@staticmethod
	async def test_control(devices):
		for i in range(len(devices)):
			try:
				await devices.endpoints[1].on_off.on()
				insertStatus() # the device was turned on 	
			except Exception as err:
				LOGGER.exception("Device is not turned on")

	@staticmethod
	def welcomeMessage(): 
		print("*********** HELLO AND WELCOME TO SECURE HOME AUTOMATION *************")
		_email = input("Enter the email you want associated with the database: ");
		return _email 

	#********** FIND A WAY TO ACCESS THE DEVICES THAT AARE ON THE NETWORK ************
if __name__ == '__main__':

	loop = asyncio.get_event_loop()
	loop.run_until_complete(ezsc_controller.setup_network())
	loop.run_until_complete(ezsc_controller.permit_join())
	
	#******** FIND A WAY TO ACCESS THE DEVICES THAT ARE ON THE NETWORK *************** 	
	print("calling _get_devices()")
	devices = asyncio.run( SHA._get_devices() )
	print(devices)
	print(len(devices))
	connector_app.insertEmail() # will insert my email 
	asyncio.run(ezsc_controller.send_command_to_turn_on_device())
	#asyncio.run(SHA.test_control(devices))
	#await devices
	#********* FOR TESTING PURPOSES ********/	
	'''while(1):
		#command = input("Enter command: ")
		for i in range(len(devices)):
			asyncio.run(ezsc_controller.send_command_to_turn_on_device(i))
			#asyncio.run(SHA.control_device(
			#asyncio.run(SHA.control_device(devices[i],"on"))
		
		time.sleep(5)'''

	
		
