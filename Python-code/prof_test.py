from ezsc import ezscApplication
import asyncio
import os
import logging
from aiohttp import web
import json
import time

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
ezsc_controller = ezscApplication()
async def permit_join(): # why request? 
	await LOGGER.info("Permitting devices to join the network for the next 60s ...")
	permit_join_future = asyncio.create_task(ezsc_controller.permit_join())
	await permit_join_future.add_done_callback(lambda futre: LOGGER.info("devices can no longer join the network"))

async def _get_devices():
	return  ezsc_controller.get_devices()

async def control_device(device, command):
	device_ieee = device["ieee"]

	try:
		await ezsc_controller.send_command(device_ieee, command, "")
		print("Your device is on")
	except Exception as e:
		 LOGGER.exception("Failed to control device!")

if __name__ == '__main__':

	loop = asyncio.get_event_loop()
	loop.run_until_complete(ezsc_controller.setup_network())
	loop.run_until_complete(ezsc_controller.permit_join())

#******** FIND A WAY TO ACCESS THE DEVICES THAT ARE ON THE NETWORK ***************      
	devices = asyncio.run(_get_devices())
	print(devices)
	print(len(devices))
#********* FOR TESTING PURPOSES ********/ 
	while(1):
		#command = input("Enter command: ")
		for i in range(len(devices)):
			asyncio.run(control_device(devices[i], "on"))

		time.sleep(5)
