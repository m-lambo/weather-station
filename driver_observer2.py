from observer2 import Publisher, Subscriber, SubscriberDB, SubscriberVisualization, SubscriberAlexa
import bme280
import smbus2
from time import sleep


port = 1
address = 0x77
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus,address)

def read_all():
    data = bme280.sample(bus,address)
    measurements = [data.humidity,data.pressure,data.temperature]
    return measurements

publisher = Publisher()

display = Subscriber('I, the compiler')
  # db = SubscriberDB(<dbObj.<table name>) ?
visualization = SubscriberVisualization('Python Graph')
interface = SubscriberAlexa('MQQT Broker')


publisher.register(display, display.update)
publisher.register(db, db.updateTable)
publisher.register(visualization, visualization.graphicallyDisplay)
publisher.register(interface, interface.transferDataToBroker)

measurements = read_all()
humidity = str(data[0])
pressure = str(data[1])
temperature = str(data[2])
publisher.dispatch(measurements)
