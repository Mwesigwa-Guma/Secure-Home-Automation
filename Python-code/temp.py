import firebase_admin
from firebase_admin import credentials  
from firebase_admin import db 

from firebase_admin import firestore
import json
from firebase import firebase

from google.cloud import firestore_v1
#**************** ADD DATA TO THE DATABAE ***************
''' NOTE: THIS WILL BE A DIFFERENT DOCUMENT '''
def addDataBase(action, status):
    doc_ref = db.reference(url='https://mobile-iot-58f29.firebaseio.com/MobleIoT/Results') # THE URL TO THE DATABASE WE WANT TO SET
    doc_ref.set({
        u'Action Name':  action,
        u'Status': status
    })

#**************** GET/READ DATA FROM THE DATABASE ************
''' NOTE: WE WANT TO GET THE DATA IN REAL TIME '''
''' NOTE: WE WANT TO READ DATA FROM SPECIFC DOCUMENT '''
''' NOTE: THIS IS THE CALL BACK FUNCTION  FOR 'firebase_admin.db.reference().listen()' '''
'''def queryDataBase(snapshot): #add 'event' as a parameter
	ref = db.reference(url='https://mobile-iot-58f29.firebaseio.com/MobleIoT/Actions')
	try:
		action = ref.get()
		print(snapshot.val())
		#print(ref.get())
		print("\n")
		print("Got the data")
	except:
		pass
	 CALL SWITCHER WHICH WHILL CALL THE FUNCTION THAT IS TO DO THE SPECIFIC ACTION
	switchAction(action)'''
def switchAction(action):
	if action == "Erastus desk on":
		erastusDeskon(action)
	elif action == "Erastus desk off":
		erastusDeskOff(action) 
	elif action == "Chris desk on":
		chrisDeskOn(action)
	elif action == "Chris desk off":
		chrisDeskOn(action)
	elif action == "Lamp on":
		lampOn(action)
	elif action == "Lamp off": 
		lampOff(action)
	elif action == "Coffee Maker on": 
		coffeeMakerOn(action)
	elif action == "Coffee Maker off": 
		coffeeMakerOff(action)
	elif action == "Turn ON LED":
		turnOnLED()
	else: 
		unrecAction(action)

#*************** ERASTUS DESK ON FUNCTION *********************
def erastuDeskOn(action): 
    	''' NOTE: THIS FUNCTION WILL TURN ON ERASTUS DEASK AND SEND THE STATUS OF IT TO THE DATABASE '''
	print("The func to turn on Erastus Desk")
	print(f"{action}") # this will print the action
	# after turn on the light update the result documen
	addDataBase(action, "Erastus Desk on ")
#****************** UNRECOGNIZE ACTION FUCTION ************************
def unrecAction(action):
	result = 'UNRECOGNIZE ACTION'
	print(action)
	addDataBase(action, result)
	
#************** MAIN PYTHON FUCNTION *************************

# call back function when the Action document changes **
def on_snapshot(document_snapshot, changes, read_time): # This is a thread that will execute in the back ground and listen for changes in the database 
	print("in snapshot")
	doc = document_snapshot
	print(u'{} => {}'.format(doc.id, doc.to_dict())) # 

	# when this works, it will give me an iterable. I will then need to parse that iterable to get the action 
	# need a function to parse the iterable.
	
	#******** THIS IS THE NEW QUERYDATABASE FUNCTION ****************

	# call a function called 'parseData' to parse the data -> it will return the action
	action = parseData(data)
	# call the 'switchAction' function and pass in the action 
	switchAction(action)
#************************ THIS FUNCTION WILL PARSE THE ITERABLE OBTAINED FROM THE DATABASE ******************
def parseData(data):
	data = str(data)
	print("I will parse the data")
	# parse the iterable
	#print(data)
	out = data[12:len(data)-2] #** This will give me the action part of the data that I need***#
	print(out)	
	return data #*** return the parsed data ***#
def main(): 
	#************** SET UP FIREBASE DATABASE ****************

	# Fetch the service account key JSON file contents 
	cred = credentials.Certificate('mobile-iot-58f29-firebase-adminsdk-tea3m-94eaf917b0.json')

	# Initialzie the app with a service account, granting admin privileges
	firebase_admin.initialize_app(cred, {'databaseURL': 'https://mobile-iot-58f29.firebaseio.com' })
	
	# As an admin , the app has access to read and write all data, regradless of Security Rules
	ref = firebase_admin.db.reference('Mobile-IoT/MobleIoT/Actions/action')

	# create a firestore client
	myClient = firebase_admin.firestore.client()
	
	actionDocRef = myClient.collection(u'MobleIoT').document(u'Actions')

	#********************** TESTING TO MAKE SURE THE DATABASE IS WORKING ***********************************		
	doc_ref = myClient.collection(u'MobleIoT').document(u'Actions')
	print(doc_ref.id)
		
	doc = doc_ref.get() # doc_ref returns a documents snapshot. 
	parseData(doc.to_dict())
	print("{}".format(doc.to_dict()))
	#*********************************************************************************************************

	# Watch the Action Document for changes  
	doc_watch = actionDocRef.on_snapshot(on_snapshot) # This will spwan a thread in the background that will continue executing 

	# the watch can be terminated
	doc_watch.unsubscribe()
	#print("end of main")	
	
	#************************** CREATE FOREVER LOOP TO EXECUTE PROGRAM ****************************
	while True:
		pass

	''' NOTE: A callback functions is called when a data change is detected *** querryDataBase()*** ''' 
	#firebase_admin.db.reference(url='https://mobile-iot-58f29.firebaseio.com/MobleIoT/Actions').on(queryDataBase)
	''' NOTE: THIS MAY NOT BE NEEDED ANYMORE ''' 
	#db = firestore.client() # create a firebase datbse client
if __name__ == "__main__":
    main()
