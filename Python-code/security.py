import crypt # used to implement salted hashes for password 
import pycrypto #used for other security schemes 
import cryptography # used for other security schemes 

#************************************************************************
#* Decrypt the data query from the database
#* Encrypt the data put into the database
#*************************************************************************

#*******************************************************************************
# I'm thinking about using public-private RSA key pairs for encryptin
# the communication between the pi and database and the App and the database
#***********************************************************************************

#*********************************************************************************
# ALSO if the RSA keys will be stored in the database, I will need to hash them. 
#*************************************************************************************

#**********************************************************************************
# TAKING into consider of the trasnfer of keys. If keys are to be automatically 
# generated, there should be method to securly transfer the keys. 
#*********************************************************************************

#************************************************************************
# This is becuase anyone with any public key can encryp with it. I want it such 
# only those in the system can encrypt using the keys
#***********************************************************************************

class Encryption: # class to encrypt data
	# This 'Encryption' class will be used to encrypt the 
	# results afte the pi has carried out the action sent from the app
	def encrypt_data(data): 

class Decryption: # class to decrypt data
	# This 'Decryption' class will be used to decrypt any message from the app
	# this may be the app publick key or an action sent from the app
	def decrypt_data(_dat): 

class Hash: # class for hasing 
	# This 'Hash' class will be used to hash the public key
	# that will be sent over to the the app
	# Do this for the app too 

class security(Encryption, Decryption, Hash): # Multiple Inheritance




#***************** AUTHENTICATION IDEA FOR LATER ***************************8
#* The user will download the app and make an account and connect their muse sensor
#* The user will download and install the prepackage OS for the raspberry pi
#* There will be commands that the user need to run to get it all working 

#************************ BIGGER IDEAD *****************************************
#* Sell the raspberry pi with all the software already installed on it.
#* all the user needs to do is power it up and register thier smart plugs 

#***********************************************************************************
