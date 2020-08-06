from observer2 import *
import bme280
import smbus2
import connectDB
from time import sleep


port = 1
address = 0x77
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus,address)

def read_all():
    data = bme280.sample(bus,address)
    measurements = [data.humidity,data.pressure,data.temperature]
    return measurements


connection = connectDB.establish_connection()
cursor = connectDB.setCursor(connection)
publisher = Publisher()

display = Subscriber('I, the compiler')
db = SubscriberDB('MariaDB', connection, cursor)
# visualization = SubscriberVisualization('Python Graph')
# interface = SubscriberAlexa('MQQT Broker')

print("Attributes for SubscriberDB::")
print(dir(db))
print("List of Publisher's dictionary elements::")
print(dir(publisher.__dict__))
publisher.register(display)
publisher.register(db, db.insert)

#  publisher.register(visualization, visualization.graphicallyDisplay)
#  publisher.register(interface, interface.transferDataToBroker)

measurements = read_all()
publisher.dispatch(measurements)
