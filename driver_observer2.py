from observer2 import *
from Measurements import *
import bme280
import smbus2
import connectDB
import constants
from time import sleep


port = 1
address = 0x77
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus,address)

def read_all():
    data = bme280.sample(bus,address)
    h = Humidity(data.humidity, constants.HUMIDITYUNITS, constants.HUMIDITYRANGE)
    p = Pressure(data.pressure, constants.PRESSUREUNITS, constants.PRESSURERANGE)
    t = Temperature(data.temperature, constants.TEMPUNITS, constants.TEMPRANGE)
    measurements = [h.getValue(),t.getValue(),p.getValue()]
    return measurements


connection = connectDB.establish_connection()
cursor = connectDB.setCursor(connection)
publisher = Publisher()

display = Subscriber('I, the compiler')
db = SubscriberDB('MariaDB', connection, cursor)
# visualization = SubscriberVisualization('Python Graph')
# interface = SubscriberAlexa('MQQT Broker')

publisher.register(display)
publisher.register(db, db.insert)

#  publisher.register(visualization, visualization.graphicallyDisplay)
#  publisher.register(interface, interface.transferDataToBroker)

print("Obtaining first reading::")
measurements = read_all()
publisher.dispatch(measurements)
print("Obtaining second reading::")
measurements = read_all()
publisher.dispatch(measurements)

