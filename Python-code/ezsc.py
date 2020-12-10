from bellows.ezsp import EZSP # This is the implementation of the EmberZNet Serial Protocol
from bellows.zigbee.application import ControllerApplication # I really don't understand this
import asyncio # python library for asynchronous frameworks that provide high-perfomance network and web-servers, database connection libraries, distrubuted task queses, etc.
import os # python library for using operating system functions 
import zigpy.endpoint # implementation of one NCP node on the network
from zigpy import types as t
import logging # python library which implement a flexiable even logging system fro applications and libraries. 

LOGGER = logging.getLogger(__name__)
#key = 'DATATBASE_FIEL'
''' This application creates a ZigBee network using bellows. 
Zigbee devices on the network will be controlled via an Android App ''' 

class ezscApplication():

	# __init__ 
	def __init__(self): 
		self.ezsp = EZSP()
		self.app = ControllerApplication(self.ezsp, os.getenv('DATABASE_FILE', "devices.db"))
	
	async def setup_network(self):
		LOGGER.info("Setting up the Zigbee network ...")
		await self.ezsp.connect(os.getenv('DEVICE', "/dev/ttyAMA0"), 115200)
		await self.app.startup(auto_form=True)
		LOGGER.info("Network setup complete!")

	async def permit_join(self): 
		await self.app.permit() # a function from bellows.zigbee.application that enbale zigbee devices to join the network. 
		await asyncio.sleep(60)

	def _ieee_to_number(self, ieee): # a function that will convert a device IEEE to readable numbers 
		ieee_string = str(t.EUI64(map(t.uint8_t, ieee)))
		return int(ieee_string.replace(':', ''), 16)

	def _get_device_by_ieee(self, ieee_to_find): # a function that returns the the device when provided the IEEE number
		for ieee, dev in self.app.devices.items(): 
			if self._ieee_to_number(ieee) == ieee_to_find: 
				return dev
		raise Excepting("Device %s is not in the device database" % (ieee_to_find,))

	def _get_cluster_by_command(self, device, command):
		for epid, ep in device.endpoints.items(): 
			if epid == 0 or not hasattr(ep, "in_clusters"): 
				continue 
		for cluster_id, cluster in ep.in_clusters.items(): 
			for server_command_id, server_command in cluster.server_commands.items():
				if command in server_command:
					return cluster
		raise Exception("Device does not support command %s!" % (command,))

	def get_devices(self):
		devices  = []

		for ieee, dev in self.app.devices.items():
			device = {
				"ieee": self._ieee_to_number(ieee), 
				"nwk": dev.nwk, 
				"endpoints": []
			}
			for epid, ep in dev.endpoints.items(): 
				if epid == 0:
					continue
				device["endpoints"].append({
					"id": epid, 
					"input_clusters": [in_cluster for in_cluster in ep.in_clusters] if hasattr(ep, "in_clusters") else [], 
					"output_clusters": [out_cluster for out_cluster in ep.out_clusters] if hasattr(ep, "out_clusters") else [],
					"status": "uninitialized" if ep.status == zigpy.endpoint.Status.NEW else "initialized"
				})
			devices.append(device)
		return devices 

	'''async def send_command(self, device_ieee, command, params=""): 
		device = self._get_device_by_ieee(device_ieee)
		LOGGER.info("sending command %s to device %s" % (command, device_ieee))
		v = await getattr(self._get_cluster_by_command(device, command), command)(*params)
		LOGGER.info(v)'''

	async def send_command_to_turn_on_device(self):
		try:
			#await self.app.endpoints[i].on_off.on()
			device = self.app.get_device("10447682632402344369")
			device.endpoint[1].on_off.on()
		except Exception as err:
			LOGGER.exception("Failed to turn on device") 
