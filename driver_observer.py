from observer import *
from Measurements import *
import bme280
import smbus2
import connectDB
import constants
import time

interval = 60 # used in loop
port = 1
address = 0x77
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus,address)

startTimeInTicks = time.time()  # setting up variables for looping function
localTime = time.localtime(time.time())
globalSeconds = localTime[5]
recording = 1

def read_all():
    data = bme280.sample(bus,address)
    h = Humidity(data.humidity, constants.HUMIDITYUNITS, constants.HUMIDITYRANGE)
    p = Pressure(data.pressure, constants.PRESSUREUNITS, constants.PRESSURERANGE)
    t = Temperature(data.temperature, constants.TEMPUNITS, constants.TEMPRANGE)
    measurements = [h.getValue(),t.getValue(),p.getValue()]
    return measurements

def startOfMinute(seconds):
    if globalSeconds == 0:
        return True
    else:
        return False

connection = connectDB.establish_connection()
cursor = connectDB.setCursor(connection)
publisher = Publisher()

display = Subscriber('The compiler')
db = SubscriberDB('MariaDB', connection, cursor)
# visualization = SubscriberVisualization('Python Graph')
# interface = SubscriberAlexa('MQQT Broker')

publisher.register(display)
publisher.register(db, db.insert)

#  publisher.register(visualization, visualization.graphicallyDisplay)
#  publisher.register(interface, interface.transferDataToBroker)


retBool = startOfMinute(globalSeconds)
while retBool is False:
    localTime = time.localtime(time.time())
    globalSeconds = localTime[5]
    retBool = startOfMinute(globalSeconds)

else:
    while recording < 10:
        localTime = time.localtime(time.time())
        globalSeconds = localTime[5]
        if globalSeconds % 10 == 0:
            retList = read_all()
            print("Obtained recording " + str(recording) + " on second " + str(globalSeconds) + " of current minute...")
            print()
            publisher.dispatch(retList)
            recording += 1
        elif recording == 10:
            print("Recorded 10 measurements")
