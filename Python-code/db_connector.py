# create all the necessary tables before hand, no need to write code for them
import mysql.connector
import logging

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level = logging.DEBUG)


class Connector: 
	@staticmethod	
	def connectToMySQL():
		try:
			'''user = "root"
			password = 
			host = "sha.cr5k1nmdho9t.us-east-2.rds.amazonaws.com"
			port = 3306
			database = "secureHomeAutomation'''
	
			cnx = mysql.connector.connect(user="root", password="", host="sha.cr5k1nmdho9t.us-east-2.rds.amazonaws.com", port=3306, database="secureHomeAutomation")
			cursor = cnx.cursor(buffered=True)
			return cursor, cnx 
		except mysql.connector.Error as err: 
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				LOGGER.exception("PROBLEM CONNECTING TO THE DATABASE! PLEASE CHECK YOUR CREDENTIALS")	
			elif err.errno == errorcode.ER_BAB_BD_ERROR:
				LOGGER.exception("Batabase does not exist")

	def qeryData(self):
		pass 
	'''def insertEmail(self): # maybe used for some other test cases
		cursor, cnx = Connector.connectToMySQL()

		add_email = "INSERT INTO smartDevices (email, ieee, deviceName, action, status) VALUES (%s, %s, %s, %s, %s)" 
		_email = ("chukpozohnt@gmail.com", "", "", "", "")

		#Insert email into table
		cursor.execute(add_email, _email)
		cnx.commit() # commits the data to the database
		cnx.close() 

		LOGGER.debug("Emaill successful commited ")'''

	def check_if_device_exists(self, _ieee): #return bool 
		cursor, cnx = Connector.connectToMySQL()
		cursor.execute("SELECT ieee FROM smartDevices")
		result = cursor.fetchall()

		for i in result:
			if i == _ieee:
				ret = True 
		if ret != True
			return False
		else 
			return ret 
	#********** FUNCTION TO INSERT A NEW DEIVCE IEEE **********
	def insertIEEE(self, _ieee): 
		cursor, cnx = Connector.connectToMySQL()
		
		add_ieee = "INSERT INTO smartDevices (ieee, deviceName, action, stauts) VALUES (%s, %s, %s, %s)"
		val = ( _ieee, "", "", "")
		
		cursor.execute(add_ieee, val)
		cnx.commit()
		cnx.close()

		LOGGER.debug("IEEE was successfully commited")
	
	def querry_ieee_and_action(): 
		cursor, cnx = Connector.connectToMySQL()
		
		# select all ieee in the database 
		cursor.execute("SELECT ieee FROM smartDevices")
		ieee_result = cursor.fetchall()

		# select all actions in the database
		cursor.execute("SELECT action FROM smartDevices")
		action_result = cursor.fetchall()
		
		return ieee_resutl, action_result
	def insertStatus(self, _status):
		cursor cnx = Connect.connectToMySQL()

		add_status = "INSERT INTO smartDevices (ieee, deviceName, action, status) VALUES (%s, %s, %s, %s)"
		val = ("", "", "", _status)

		cursor.execute(add_iee, val)
		cnx.commit()
		cnx.close()

		LOGGER.deug("Status was successfully commited") 
	
	# A function to listen for changes in the Action column 


if __name__ == '__main__':
	_myConnector = Connector()
	Connector.connectToMySQL()
	_myConnector.insertEmail()
