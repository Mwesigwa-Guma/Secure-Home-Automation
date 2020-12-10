## *** THIS FILE IS MEANT TO TEST THE CRITICAL CODES AS I WRITE IT **** 

from ezsc import ezscApplication
import asyncio
import os
import logging

ezsc_app = ezscApplication()


if __name__ == '__main__':
	# write the test here 
	#ezsc_app.calc_test(2, 3) # this is how you test a function in python 

	loop = asyncio.get_event_loop()
	loop.run_until_complete(ezsc_app.setup_network())
	
