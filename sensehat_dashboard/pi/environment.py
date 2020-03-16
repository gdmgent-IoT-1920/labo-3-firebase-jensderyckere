from sense_hat import SenseHat
import threading
import firebase_admin
from firebase_admin import credentials, firestore

# constants
COLLECTION = 'raspberry'
DOCUMENT = 'omgeving'

# firebase
cred = credentials.Certificate("../config/firebase_admin.json")
firebase_admin.initialize_app(cred)

# connect firestore
db = firestore.client()
pi_ref = db.collection(COLLECTION).document(DOCUMENT)


# sense
sense = SenseHat()

# sensors
temp = sense.get_temperature()
hum = sense.get_humidity()
temp_hum = sense.get_temperature_from_humidity()
temp_pres = sense.get_temperature_from_pressure()
pres = sense.get_pressure()

data = {
	u'temperature' : temp,
	u'humidity' : hum,
	u'humidity temperature' : temp_hum,
	u'pressure' : pres,
	u'pressure temperature' : temp_pres,
}

# interval
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

# firebase send data
def send_data():
	pi_ref.set(data)
	print('aangepast')

timer = set_interval(send_data, 300)